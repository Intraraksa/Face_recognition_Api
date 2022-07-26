from pydantic import BaseModel

class Client_detail(BaseModel):
    IdCard:int
    name_lastname:str
    embedding:list = []
