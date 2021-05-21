import cv2

img = cv2.imread('imgex.jpg', cv2.IMREAD_GRAYSCALE) # 2를 넣을시 흑백

cv2.imwrite('imgexsave.jpg', img) # 저장 

print(img) # numpy 형식으로 된 3차원 배열. [b, g, r] 형태로 들어옴
    
cv2.imshow('gray', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()
