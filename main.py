from utils import utils
import cv2

image = cv2.imread("images/test.png")
utils.SlicedDetection(image,model="yolov4")

cv2.imshow("Window", image)
cv2.imwrite("result.png",image)
cv2.waitKey()
cv2.destroyAllWindows()