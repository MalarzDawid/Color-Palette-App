from io import BytesIO

import cv2
import numpy as np
from PIL import Image


def read_image(upload_image) -> Image.Image:
    """Load uploaded image and transform to numpy array"""
    image = Image.open(BytesIO(upload_image))
    return image


def preprocess(image: Image.Image) -> np.ndarray:
    # Prepare image
    data = np.array(image)
    height, width, _ = np.shape(image)
    data = np.reshape(image, (height * width, 3))
    data = np.float32(data)
    return data


def cv_clustering(image: np.ndarray, clusters: int) -> np.ndarray:
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    _, _, centers = cv2.kmeans(image, clusters, None, criteria, 10, flags)
    return centers


def values_to_dict(values: np.ndarray) -> dict:
    values_dict = {}
    for idx, color in enumerate(values):
        colors = {"r": int(color[0]), "g": int(color[1]), "b": int(color[2])}
        values_dict[idx] = colors
    return values_dict
