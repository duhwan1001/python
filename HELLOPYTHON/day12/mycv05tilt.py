import cv2

img = cv2.imread('imgex.jpg', cv2.IMREAD_GRAYSCALE)  # 2를 넣을시 흑백

print(img.shape[:2])

(h, w) = img.shape[:2]

center = (w / 2, h / 2)

Mat = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(img, Mat, (w, h))

cv2.imshow('gray', rotated)
cv2.waitKey(0) 
cv2.destroyAllWindows()
