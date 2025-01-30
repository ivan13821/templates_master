
from fastapi import FastAPI, Body, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from typing import Annotated
import os
import asyncio


from actions_with_files.main import FileAction


app = FastAPI()





async def trash_killer(filename):
    """Убивает ненужные файлы"""

    await asyncio.sleep(5)


    os.remove(f"created/{filename}.pdf")
    








#Получение данных формы для заполнения шаблона 
@app.post("/")
async def generate_pdf(data = Body()):


    file_name = data["file_name"]
    task = asyncio.create_task(trash_killer(filename=file_name))
    del data["file_name"]

    return FileAction.generete_pdf(context=data["context"], file_name=file_name)







#Скачивание файла пользователем
@app.get("/file/download")
def download_file(data = Body()):

    try:
        filename = data["filename"]
        return FileResponse(path=f'templates/{filename}.docx', filename=f'{filename}.docx', media_type='multipart/form-data')
    except KeyError:
        return {"message": "file is not exists"}



#Скачивание файла полученного от пользователя
@app.post("/upload")
def upload(file: UploadFile = File(...)):

    message = FileAction.save_file(file=file)

    return {"message": message}


