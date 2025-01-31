















class DataVerification:

    """Класс для проверки данных"""



    @staticmethod
    def key_in_json(key: any, json: dict) -> bool:

        """ Проверяет есть ли ключ в json"""

        return key not in json.keys()
    



    @staticmethod
    def get_file(json: dict) -> bool:
        """Проверяет соответствует ли json нужному """

        
        for i in ["meta_data", "tables", "context", "download_type", "file_name"]:
            if i not in json.keys(): return False
        

        if type(json["tables"]) == dict and type(json["context"]) == dict and type(json["meta_data"]) == dict:
            return True
        
        return False