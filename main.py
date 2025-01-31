
from fastapi import FastAPI, Body, UploadFile, File
import asyncio


from repository.files import FileAction
from service.handler import Handler
from service.data_verification import DataVerification
from models.main import *

app = FastAPI()










#Получение данных формы для заполнения шаблона 
@app.post("/gen")
async def generate_pdf(data = Body()):
    if not DataVerification.get_file(data): return {"error": "missing json"}
    file_name = data["file_name"]
    task =asyncio.create_task(FileAction.trash_killer(filename=file_name))
    return FileAction.generete_pdf(context=data["context"], file_name=file_name)







#Скачивание файла пользователем
@app.get("/download")
def download_file(data: DownloadFile):
    return FileAction.get_file_response(folder="templates", filename=data.filename)






#Скачивание файла полученного от пользователя
@app.post("/add")
def upload(file: UploadFile = File(...)):
    message = FileAction.save_file(file=file)
    return {"message": message}






#Удаление файла пользователем
@app.delete("/delete")
def delete_file(data: DelFile):
    return {"message":FileAction.del_file(filename=data.filename)}


