from enum import Enum

import uvicorn
from fastapi import FastAPI, File, UploadFile

from dominant.clustering import cv_clustering
from dominant.utils import preprocess, read_image, values_to_dict

app = FastAPI()


class ClusteringType(str, Enum):
    opencv = "opencv"
    sklearn = "sklearn"


@app.get("/")
def read_about() -> None:
    return {"About": "Load image and create a color palette"}


@app.post("/get_palette")
async def get_palette(
    clustering_type: ClusteringType, file: UploadFile = File(...), clusters: int = 3
) -> dict:
    image = read_image(await file.read())
    image_preprocess = preprocess(image)
    if clustering_type == "opencv":
        values = cv_clustering(image_preprocess, clusters)
    if clustering_type == "sklearn":
        return {"palette": "Not work"}
    output = values_to_dict(values)
    return {"palette": output}


def start() -> None:
    uvicorn.run("dominant.main:app", host="0.0.0.0", port=8000, reload=True)
