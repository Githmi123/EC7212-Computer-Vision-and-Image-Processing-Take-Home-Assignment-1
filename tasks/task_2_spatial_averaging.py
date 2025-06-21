import cv2
import os

os.makedirs("../results", exist_ok=True)
img = cv2.imread('../images/task2.jpg')
if img is None:
    print("Image not found!")
    exit(1)

blur_3x3 = cv2.blur(img, (3, 3))
output_filename = f"../results/task2_blur_3x3.jpg"
cv2.imwrite(output_filename, blur_3x3)

blur_10x10 = cv2.blur(img, (10, 10))
output_filename = f"../results/task2_blur_10x10.jpg"
cv2.imwrite(output_filename, blur_10x10)

blur_20x20 = cv2.blur(img, (20, 20))
output_filename = f"../results/task2_blur_20x20.jpg"
cv2.imwrite(output_filename, blur_20x20)

print("Blurred images saved successfully in the 'results' directory.")


