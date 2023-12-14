import cv2
import time
from picamera2 import Picamera2
from libcamera import Transform, controls

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}, transform=Transform(hflip=True, vflip=True)))
picam2.set_controls({'AfMode': controls.AfModeEnum.Continuous})
picam2.start()

i = 0
while True:
    im = picam2.capture_array()
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Camera", im)
    if i < 100:
        cv2.imwrite(f"./OK/image{i}.png", grey)
        time.sleep(1)

    key = cv2.waitKey(1)
    if key == 27:
        break
    i += 1
