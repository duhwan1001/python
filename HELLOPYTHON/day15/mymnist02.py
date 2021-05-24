# 필요한 라이브러리 불러오기
import cv2
from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

for i, img in enumerate(train_images):
    cv2.imwrite("test/" + str(test_labels[i]) + "_" + str(i) + ".jpg", img)
    if i > 100:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()

