from dominant import __version__
from dominant.utils import values_to_dict
import numpy as np


def test_utils_values_to_dict():
    rgb_values = np.array([[127, 255, 195]])
    output = {
        0: {
            "r": 127,
            "g": 255,
            "b": 195
        }
    }
    assert output == values_to_dict(rgb_values)


def test_version():
    assert __version__ == '0.1.0'
