import  numpy as np
import  cv2

img = cv2.imread('images/1_03b_0.png')

def graying(img):
    row, col, channel = img.shape
    img_gray=np.zeros((row,col),np.uint8)

    for r in range(row):
        for c in range(col):
            img_gray[r,c] = 0.11 * img[r,c,0] + 0.59*img[r,c,1] + 0.3*img[r,c,2]

    return img_gray

cv2.imshow('img_gray',graying(img))
cv2.imwrite('gray.jpg',graying(img))
cv2.waitKey(0)