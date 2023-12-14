import cv2
import numpy

_ = cv2.imread("OK/image0.png", cv2.IMREAD_GRAYSCALE)
tmp = numpy.zeros(_.shape)
print(tmp)

for i in range(100):
    im = cv2.imread(f"OK/image{i}.png", cv2.IMREAD_GRAYSCALE)
    tmp += im

cv2.imwrite("OK/ave.png", tmp / 100.0)
