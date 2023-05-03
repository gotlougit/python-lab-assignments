import cv2

# Load color image
img = cv2.imread('image.jpg')

# Extract pixel values in red, green, and blue dimensions
b, g, r = cv2.split(img)

# Print first 5 pixel values in each dimension
print(f"Blue pixels: {b[:5]}")
print(f"Green pixels: {g[:5]}")
print(f"Red pixels: {r[:5]}")
