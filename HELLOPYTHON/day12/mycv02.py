import cv2 as cv

img = cv.imread('imgex.jpg', 2) # 2를 넣을시 흑백

print(img) # numpy 형식으로 된 3차원 배열. [b, g, r] 형태로 들어옴

cv.imshow('display', img)

cv.waitKey(0)

cv.destroyAllWindows()