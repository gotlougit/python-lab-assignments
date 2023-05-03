import cv2

# Read gray image
img_gray = cv2.imread('gray_image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply thresholding to convert to binary image
threshold = 127
max_val = 255
ret, img_binary = cv2.threshold(img_gray, threshold, max_val, cv2.THRESH_BINARY)

# Save both images
cv2.imwrite('gray_image.jpg', img_gray)
cv2.imwrite('binary_image.jpg', img_binary)
