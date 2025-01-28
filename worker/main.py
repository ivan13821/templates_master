from docxtpl import DocxTemplate
from docx2pdf import convert
import os


class MyFile():

    """ Класс для заполнения шаблонов """


    @staticmethod
    def generete_txt(context: dict, file_name: str):

        """Передайте этой функции json где ключ это поле в таблице, а значение то что нужно вставить """

        
        if not MyFile.test(folder="templates", file_name=file_name): return "Нет такого файла в корневой директории!"
        
        doc = DocxTemplate(f"templates/{file_name}.docx")

        created_folder = 'created'
        

        postfix = '1'
        doc.render(context)
        doc.save(f"{created_folder}/{file_name}{postfix}.docx")


        convert(f"{created_folder}/{file_name}{postfix}.docx")

        os.remove(f"{created_folder}/{file_name}{postfix}.docx")













    
    @staticmethod
    def test(folder: str, file_name: str) -> bool:

        try:
            open(f"{folder}/{file_name}.docx")
            return True
        except: return False 