import cv2
import numpy as np


def cv_clustering(image: np.ndarray, clusters: int) -> np.ndarray:
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    _, _, centers = cv2.kmeans(image, clusters, None, criteria, 10, flags)
    return centers
