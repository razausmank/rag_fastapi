from pydantic import BaseModel

class ItemBase(BaseModel): 
    name: str
    description : str 

class ItemRead(ItemBase):
    pass 

class ItemCreate(ItemBase): 
    pass 