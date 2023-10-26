# OpenCV2 パターンマッチング

前回紹介した SAD はわかりやすいが、外乱（ノイズ）に弱い。より良い方法がさまざま研究・開発されている。
今回紹介する方法は AI (人工知能) ではなく、あくまで計算 (数学) で「もっとも近しい」ところを見つけ出している。

これらは colaboratory でも試すことができる。

# サンプル画像

## ２値画像

白と黒の点で作られた画像。

### マッチング対象
<img src="./images/sample_vegi_2.png" width="80%"/>

### マッチングパターン
<img src="./images/sample_vegi_2_pat.png" width="15%"/>

### サンプルプログラム

``` python
import cv2

# ファイルを読み込む
img = cv2.imread("sample_vegi_2.png")
template = cv2.imread('sample_vegi_2_pat.png')
(h, w, c) = template.shape

# マッチング処理
res = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)
(min_val, max_val, min_loc, max_loc) = cv2.minMaxLoc(res)

# 四角で囲う
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img, top_left, bottom_right, (0,0,255), 2)

# ファイルに書き出す
cv2.imwrite("result_2.png", img)
```

## グレースケール

真っ白 (255) から真っ黒 (0) まで 256 段階で色分けした画像。

### マッチング対象
<img src="./images/sample_vegi_gray.png"/>

### マッチングパターン
<img src="./images/sample_vegi_gray_pat.png" width="15%"/>

### サンプルプログラム

``` python
import cv2

# ファイルを読み込む
img = cv2.imread("sample_vegi_gray.png")
template = cv2.imread('sample_vegi_gray_pat.png')
(h, w, c) = template.shape

# マッチング処理
res = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)
(min_val, max_val, min_loc, max_loc) = cv2.minMaxLoc(res)

# 四角で囲う
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img, top_left, bottom_right, (0,0,255), 2)

# ファイルに書き出す
cv2.imwrite("result_2.png", img)
```
## カラー画像

### マッチング対象
<img src="./images/sample_vegi.png" witdh="70%"/>

### マッチングパターン
<img src="./images/sample_vegi_pat.png" width="15%"/>

### サンプルプログラム

```
自分で書いてみよう
```

# 正規化相関係数 (TM_CCOEFF_NORMED)

もっとも頑健 (がんけん。丈夫、頑丈。ノイズに強い)。ただし計算がめんどくさい (コンピュータに負荷になる)。コンピュータが速いときにはこいつを使えばいい。
1 が最も似ている。0 が無相関。-1 は正反対。  
「ピアソンの相関係数」という値。

# 相関係数 (TM_CCOFF)

正規化相関係数は -1 ~ +1 の間に収まるようになっているが、それの計算を省いた。つまり相関値の範囲は画像次第。

# 正規化二乗差 (TM_SQDIFF_NORMED)

SAD は単純に引いたものの絶対値を足していたが、SQDIFF は引いたものを２乗して足し込む。ずれればずれるほど、差が広がる。
「正規化」は 0~1の範囲に収まるようにしたよ、という意味。
処理が簡単なので、コンピュータの負荷が軽い。ただし精度とのトレードオフ。

# 二乗差 (TM_SQDIFF)
引いたものの２乗して足し込む。
処理が簡単なので、コンピュータの負荷が軽い。ただし精度とのトレードオフ。

# 相互相関 (TM_CCORR)
画像を行列と見立て、内積 (掛け算) を求めたもの。傾向が似ていれば大きくなる。
(工業数学でやったけど覚えてる？)

# 正規化相互相関 (TM)
上の相互相関を -1 ~ 1 の範囲に収まるようにしたもの。
