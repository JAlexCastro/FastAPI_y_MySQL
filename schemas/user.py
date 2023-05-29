#Package Python
from typing import Optional

#Package Pydantic
from pydantic import BaseModel


class User(BaseModel):
    id : Optional[int]
    name : str
    last_name: str
    email : str
    password : str