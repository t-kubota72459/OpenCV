import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("sample_vegi_gray.png")
template = cv2.imread('sample_vegi_gray_pat.png')
(h, w, c) = template.shape
print(w, h)

res = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)
(min_val, max_val, min_loc, max_loc) = cv2.minMaxLoc(res)
print(min_val, max_val, min_loc, max_loc)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img, top_left, bottom_right, (0,0,255), 2)

cv2.imwrite("result_gray.png", img)
