from io import BytesIO
from typing import List, Tuple, Union

import numpy as np
from PIL import Image


def read_image(upload_image) -> Image.Image:
    """Load uploaded image and transform to numpy array"""
    image = Image.open(BytesIO(upload_image))
    return image


def preprocess(image: Image.Image) -> np.ndarray:
    data = np.array(image)
    height, width, _ = np.shape(image)
    data = np.reshape(image, (height * width, 3))
    data = np.float32(data)
    return data


def values_to_dict(values: np.ndarray) -> dict:
    values_dict = {}
    for idx, color in enumerate(values):
        colors = {"r": int(color[0]), "g": int(color[1]), "b": int(color[2])}
        values_dict[idx] = colors
    return values_dict


def create_bar(
    height: int, width: int, color: List[float]
) -> Union[np.ndarray, Tuple[float]]:
    bar = np.zeros(shape=(height, width, 3), dtype=np.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    return bar, (red, green, blue)


def create_palette(values: np.ndarray) -> np.ndarray:
    bars = []
    rgb_values = []
    for _, row in enumerate(values):
        bar, rgb = create_bar(150, 150, row)
        bars.append(bar)
        rgb_values.append(rgb)
    img_bar = np.hstack(bars)
    return img_bar
