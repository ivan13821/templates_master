
from fastapi import UploadFile, HTTPException
from docxtpl import DocxTemplate
from docx2pdf import convert
import os
from fastapi.responses import FileResponse











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

        try:
            open(f"{folder}/{file_name}.docx")
            return True
        except: return False 