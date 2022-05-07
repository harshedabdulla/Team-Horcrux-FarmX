from fastapi import FastAPI, Body, Request, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import ml_model as mml

import base64

from PIL import Image
import io

import tensorflow as tf

app=FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="static")

@app.get("/")
async def example(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submitform")
async def handle_form(file_uploaded: UploadFile=File(UploadFile)):
    img_content= await file_uploaded.read()
    # print(img_content)
    base64_bytes = base64.b64encode(img_content)
    base64_string = base64_bytes.decode("ascii")
    # print(base64_string)
    image = base64.b64decode(str(base64_string))
    img = Image.open(io.BytesIO(image))
    img.save("image.jpg", 'jpeg')
    
    # my_model = mml.build_model()
    # mml.train(my_model, "./rice_leaf_diseases") # dataset location
    # my_model.save("trained_model.h5")

    my_model = tf.keras.models.load_model("trained_model.h5")
    pred = int(mml.test(my_model, "image.jpg")) # test image location
    res = ""
    if pred == 0:
        res = "bacterial"
    elif pred == 1:
        res = "brown spot"
    else:
        res = "lead smut"
    return {
        "identified as:": res 
    }




