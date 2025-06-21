import cv2
import os

os.makedirs("../results", exist_ok=True)
img = cv2.imread("../images/task3.jpg")
if img is None:
    print("Image not found!")
    exit(1)

# Get the image center
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
print("Image Shape: ", img.shape)

# 45 is a custom angle, so we need to use this method
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_img_45 = cv2.warpAffine(img, rotation_matrix, (w, h))

# 90 is an exact multiple of 90, so we can use this method
rotated_img_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

output_filename = f"../results/task3_rotated_img_45.jpg"
cv2.imwrite(output_filename, rotated_img_45)

output_filename = f"../results/task3_rotated_img_90.jpg"
cv2.imwrite(output_filename, rotated_img_90)

print("Rotated images saved successfully in the 'results' directory.")