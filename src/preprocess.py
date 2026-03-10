import cv2


def preprocess_image(image_path):
    """
    Preprocess the input image to make shape detection easier.

    Steps:
    1. Load image
    2. Convert to grayscale
    3. Apply Gaussian Blur
    4. Adaptive Threshold
    5. Canny Edge Detection
    """

    # Load image
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce noise using Gaussian blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Adaptive threshold for hand-drawn diagrams
    thresh = cv2.adaptiveThreshold(
        blur,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11,
        2
    )

    # Detect edges
    edges = cv2.Canny(thresh, 50, 150)

    return image, edges