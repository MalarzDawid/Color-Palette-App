import uvicorn
from fastapi import FastAPI, File, UploadFile

from dominant.clustering import cv_clustering
from dominant.utils import preprocess, read_image, values_to_dict

app = FastAPI()


@app.get("/")
def read_about() -> None:
    return {"About": "Load image and create a color palette"}


@app.post("/get_palette")
async def create_upload_file(file: UploadFile = File(...), clusters: int = 3) -> dict:
    image = read_image(await file.read())
    image_preprocess = preprocess(image)
    values = cv_clustering(image_preprocess, clusters)
    output = values_to_dict(values)
    return {"palette": output}


def start() -> None:
    uvicorn.run("dominant.main:app", host="0.0.0.0", port=8000, reload=True)
