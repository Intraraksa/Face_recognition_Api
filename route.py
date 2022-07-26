from fastapi import APIRouter
from schema import table
from database import Client_detail

router = APIRouter()

@router.get('/')
async def home():
    return {"This is face recognition app":"Botnoi"}

@router.get('/find_client/{id}')
async def find_client(id : int):
    z = table.find_one({"Idcard":id})
    data = [z[j] for j in[i for i in z.keys() if i != "_id"]][:2]
    return data

@router.post("/add_client/")
async def add_client(data : Client_detail):
    info = {"Idcard" : data.IdCard ,
            "name" : data.name_lastname,
            "face_emb" : data.embedding}
    table.insert_one(info)
    return {"Insert :":{data.IdCard}}

@router.put('/update_name/{idcard}/{name}')
async def update_name(idcard : int , name : str):
    query = {"Idcard" : idcard}
    new_data = {"$set" : {"name":name}}
    table.update_one(query,new_data)
    return {"Update " : {idcard : name}}

