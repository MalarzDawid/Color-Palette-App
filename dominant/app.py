import streamlit as st
from PIL import Image

from dominant.clustering import cv_clustering
from dominant.utils import create_palette, preprocess

st.title("Color palette - App")

upload_image = st.file_uploader("Choose an image...", type="jpg")


if upload_image is not None:
    orginal_image = Image.open(upload_image)

    image = preprocess(orginal_image)

    st.image(orginal_image, caption="Uploaded image", use_column_width=True)

    number_of_clusters = st.number_input(
        "Number of clusters: ", min_value=1, max_value=6, value=3, step=1
    )

    # Clustering
    values = cv_clustering(image, number_of_clusters)
    color_palette = create_palette(values)

    st.image(color_palette, caption="Color palette")
