import cv2
import time
from picamera2 import Picamera2
from libcamera import Transform, controls

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}, transform=Transform(hflip=True, vflip=True)))
picam2.set_controls({'AfMode': controls.AfModeEnum.Continuous})
picam2.start()

ref = cv2.imread("./battery.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("REFERENCE", ref)

ref_shape = ref.shape

i = 0
while True:
    im = picam2.capture_array()
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(grey, ref, cv2.TM_CCOEFF_NORMED)
    (min_v, max_v, min_l,max_l) = cv2.minMaxLoc(res)

    x0 = max_l[0]
    y0 = max_l[1]

    x1 = x0 + ref_shape[1]
    y1 = y0 + ref_shape[0]

    cv2.rectangle(im, (x0, y0), (x1, y1), (255,0,0), 2, cv2.LINE_AA)
    cv2.putText(im, f"{max_v:.3f}", (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255),2, cv2.LINE_AA)
    cv2.imshow("Camera", im)
    key = cv2.waitKey(1)
    if key == 27:
        break
