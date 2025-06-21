import cv2
import numpy as np
import os

def get_block_average(img, block_size):
    h, w = img.shape[:2]
    output = np.zeros_like(img) # Create an empty output image of the same shape

    if len(img.shape) == 2:  # Grayscale image
        print("Grayscale image detected.")
        for y in range(0, h, block_size):
            for x in range(0, w, block_size):
                y_end = min(y + block_size, h) # Define the block boundaries (ensure no overflow at edges)
                x_end = min(x + block_size, w)

                block = img[y:y_end, x:x_end] # Extract the block
                avg = np.uint8(np.mean(block))

                output[y:y_end, x:x_end] = avg

    elif len(img.shape) == 3:  # Color image
        print("Color image detected.")
        channels = img.shape[2]
        for y in range(0, h, block_size):
            for x in range(0, w, block_size):
                y_end = min(y + block_size, h)
                x_end = min(x + block_size, w)
                for c in range(channels): # Process each channel separately
                    block = img[y:y_end, x:x_end, c]
                    avg = np.uint8(np.mean(block))

                    output[y:y_end, x:x_end, c] = avg

    else:
        raise ValueError("Unsupported image format.")

    return output



def main():
    os.makedirs("../results", exist_ok=True)
    # img = cv2.imread("../images/task4.jpg") # Uncomment to load as color image
    img = cv2.imread("../images/task4.jpg", cv2.IMREAD_GRAYSCALE) # Uncomment to load as grayscale image

    if img is None:
        print("Image not found!")
        exit(1)

    for block_size in [3, 5, 7]:
        # result = get_block_average(img, block_size)
        result = get_block_average(img, block_size)
        if len(img.shape) == 2:
            filename = f"../results/task4_block_average_for_grayscale_{block_size}.jpg"
        elif len(img.shape) == 3:
            filename = f"../results/task4_block_average_for_color_{block_size}.jpg"
        else:
            raise ValueError("Unsupported image format.")
        cv2.imwrite(filename, result)
    print("Block averaged images saved successfully in the 'results' directory.")


if __name__ == "__main__":
    main()

