import cv2
img_path="pic.png"
img=cv2.imread(img_path)

ret,thresh = cv2.threshold(img,70,255,0)

cv2.imshow("img_bin",thresh)

cv2.imshow("img_gray",img)

print(thresh)

print(img)

cv2.waitKey(0)
