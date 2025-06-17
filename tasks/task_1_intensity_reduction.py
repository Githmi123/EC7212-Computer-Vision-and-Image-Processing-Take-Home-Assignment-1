import cv2
import numpy as np
import os

def reduce_intensity_levels(img, levels):
    if (levels < 2 or levels > 256):
        raise ValueError("Levels must be between 2 and 256 inclusive.")

    desired_levels = 2 ** i for i in range(1, 9)

    if levels not in desired_levels:
        raise ValueError("Levels must be one of the following: 2, 4, 8, 16, 32, 64, 128, 256")

    factor = 256 // levels
    reduced_img = (img // factor) * factor
    return reduced_img

if __name__ == "__main__":
    img = cv2.imread("../images/task1.jpg", cv2.IMREAD_GRAYSCALE) # loaded as a numpy array
    
    if img is None:
        print("Error: Image not found.")
        exit(1)

    print("Original Image Shape: ", img.shape)
    
    levels = int(input("Enter the number of intensity levels (2-256, in integer poers of 2): "))

    try:
        output_img = reduce_intensity_levels(img, levels) # applies the division to all pixels at once
        os.makedirs("../results", exist_ok=True)
        output_filename = f"../results/task1_reduced_intensity_levels_{levels}.jpg"
        cv2.imwrite(output_filename, output_img)
    except ValueError as e:
        print(e)




