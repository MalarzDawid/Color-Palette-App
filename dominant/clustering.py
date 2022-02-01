import cv2
import numpy as np
from sklearn.cluster import KMeans


def cv_clustering(image: np.ndarray, clusters: int) -> np.ndarray:
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    _, _, centers = cv2.kmeans(image, clusters, None, criteria, 10, flags)
    return centers


def sklearn_clustering(image: np.ndarray, clusters: int) -> np.ndarray:
    # TODO
    kmeans = KMeans(n_clusters=clusters, random_state=2022).fit(image)
    labels = np.arange(0, len(np.unique(kmeans.labels_)) + 1)
    (hist, _) = np.histogram(kmeans.labels_, bins=labels)
    hist = hist.astype(np.float32)
    hist /= hist.sum()
    return hist * 255
