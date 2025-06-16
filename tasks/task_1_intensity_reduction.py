import cv2

if __name__ == "__main__":
    img = cv2.imread("../images/task1.jpg", cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print("Error: Image not found.")
        exit(1)

    print("Original Image Shape: ", img.shape)
    