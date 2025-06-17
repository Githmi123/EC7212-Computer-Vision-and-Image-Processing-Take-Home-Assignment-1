import cv2
import os

if __name__ == "__main__":
    os.makedirs("../results", exist_ok=True)
    img = cv2.imread('../images/task2.jpg', cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Image not found!")
        exit(1)
    
    blur_3x3 = cv2.blur(img, (3, 3))
    output_filename = f"../results/task2_blur_3x3.jpg"
    cv2.imwrite(filename, blur_3x3)


