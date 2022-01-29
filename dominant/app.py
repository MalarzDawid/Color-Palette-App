import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Dominant App")

upload_image = st.file_uploader("Choose an image...", type="jpg")


def create_bar(height, width, color):
    bar = np.zeros(shape=(height, width, 3), dtype=np.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    return bar, (red, green, blue)


if upload_image is not None:
    image = Image.open(upload_image)

    # Prepare image input
    data = np.array(image)
    height, width, _ = np.shape(image)
    data = np.reshape(image, (height * width, 3))
    data = np.float32(data)

    st.image(image, caption="Uploaded image", use_column_width=True)

    number_clusters = st.number_input(
        "Number of clusters: ", min_value=1, max_value=6, value=3, step=1
    )

    # Clustering
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    compactness, label, centers = cv2.kmeans(
        data, number_clusters, None, criteria, 10, flags
    )

    bars = []
    rgb_values = []
    for index, row in enumerate(centers):
        bar, rgb = create_bar(150, 150, row)
        bars.append(bar)
        rgb_values.append(rgb)
    img_bar = np.hstack(bars)
    st.image(img_bar, caption="Color palette")
