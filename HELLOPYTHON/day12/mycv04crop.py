import cv2

img = cv2.imread('imgex.jpg', cv2.IMREAD_GRAYSCALE) # 2를 넣을시 흑백

print(len(img))
print(len(img[0]))

crop_img = img[150:350, 650:850]

cv2.imshow('gray', crop_img)

cv2.imwrite('cropImg.jpg',crop_img)
cv2.waitKey(0) 
cv2.destroyAllWindows()
