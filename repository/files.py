
from fastapi import UploadFile, HTTPException
from docxtpl import DocxTemplate
from docx2pdf import convert
import os
from fastapi.responses import FileResponse
import asyncio









class FileAction:

    """ Осуществляет различные действия с файлами """



    @staticmethod
    def save_file(file: UploadFile) -> str:

        """ Созраняет файл в папку templates """

        try:
            open(f"templates/{file.filename}")
            return {"message": "file already exists"}
        
        except:
            try:
                contents = file.file.read()
                with open(f"templates/{file.filename}", 'wb') as f:
                    f.write(contents)
            except Exception:
                raise HTTPException(status_code=500, detail='Something went wrong')
            finally:
                file.file.close()
            
            return {"message": f"Successfully uploaded {file.filename}"}
        
        

    @staticmethod
    def generete_pdf(context: dict, file_name: str):

        """Передайте этой функции json где ключ это поле в таблице, а значение то что нужно вставить """

        
        if not FileAction.test(folder="templates", file_name=file_name): return "Нет такого файла в корневой директории!"
        
        doc = DocxTemplate(f"templates/{file_name}.docx")

        created_folder = 'created'
        


        doc.render(context)
        doc.save(f"{created_folder}/{file_name}.docx")


        convert(f"{created_folder}/{file_name}.docx")

        os.remove(f"{created_folder}/{file_name}.docx")

        let = FileResponse(path=f'created/{file_name}.pdf', filename=f'{file_name}.pdf', media_type='multipart/form-data')

        return let




    
    @staticmethod
    def test(folder: str, file_name: str) -> bool:

        """Проверяет наличие файла в директории"""

        try:
            open(f"{folder}/{file_name}.docx")
            return True
        except: return False 
    








    @staticmethod
    async def trash_killer(filename: str):

        """Убивает ненужные файлы спустя 5 секунд после вызова"""

        await asyncio.sleep(5)

        try:
            os.remove(f"created/{filename}.pdf")
        except:
            pass
    




    @staticmethod
    def del_file(filename: str, folder: str = "templates") -> str:
        
        """Удаляет файл из каталога """
        print(os.listdir(folder))

        if f"{filename}.docx" in os.listdir(folder):
            os.remove(f"{folder}/{filename}.docx")
            return {"message":"file deleted"}
        else:
            return {"message": "no such file exists"}
    



    @staticmethod
    def get_file_response(filename: str, folder: str = "templates"):

        if f"{filename}.docx" in os.listdir(folder):
            return FileResponse(path=f'{folder}/{filename}.docx', filename=f'{filename}.docx', media_type='multipart/form-data')
        else:
            return {"message": "file is not exists"}