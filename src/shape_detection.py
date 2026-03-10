import cv2
import numpy as np


def detect_shapes(image, edges):
    """
    Detect geometric shapes from the edge image.

    Returns:
    - image with bounding boxes
    - dictionary with shape counts
    """

    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    shape_counts = {
        "Triangle": 0,
        "Rectangle": 0,
        "Square": 0,
        "Circle": 0
    }

    for contour in contours:

        # Ignore very small contours
        if cv2.contourArea(contour) < 100:
            continue

        # Approximate polygon
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        vertices = len(approx)

        shape = "Unknown"

        # Shape classification
        if vertices == 3:
            shape = "Triangle"

        elif vertices == 4:

            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = w / float(h)

            if 0.95 <= aspect_ratio <= 1.05:
                shape = "Square"
            else:
                shape = "Rectangle"

        elif vertices > 4:
            shape = "Circle"

        # Update count
        if shape in shape_counts:
            shape_counts[shape] += 1

        # Draw bounding box
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Label shape
        cv2.putText(
            image,
            shape,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 255),
            2
        )

    return image, shape_counts