from worker.main import MyFile
from fastapi import FastAPI, Body


app = FastAPI()

@app.post("/")
async def generate_pdf(data = Body()):

    file_name = data["file_name"]
    del data["file_name"]

    MyFile.generete_txt(context=data, file_name=file_name)

    return {"body":"created!!!"}