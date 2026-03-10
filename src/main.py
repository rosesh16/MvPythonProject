import os
import cv2

from preprocess import preprocess_image
from shape_detection import detect_shapes


DATASET_PATH = r"C:\Users\ASUS\MvPython\data\dataset\images"


def process_images():

    # Loop through all images
    for filename in os.listdir(DATASET_PATH):

        # Process only image files
        if filename.endswith(".png") or filename.endswith(".jpg"):

            image_path = os.path.join(DATASET_PATH, filename)

            print("\n========================")
            print("Processing Image:", filename)

            # Preprocess image
            image, edges = preprocess_image(image_path)

            # Detect shapes
            result, counts = detect_shapes(image, edges)

            print("Detected Shapes:")

            for shape, count in counts.items():
                print(f"{shape}: {count}")

            # Display results
            cv2.imshow("Detected Shapes", result)
            cv2.imshow("Edges", edges)

            cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    process_images()