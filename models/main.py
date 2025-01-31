from pydantic import BaseModel





class DownloadFile(BaseModel):
    filename: str





class DelFile(BaseModel):
    filename: str
