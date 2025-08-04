from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    age: int
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    age: int
    email: str

    class Config:
        from_attributes = True  # instead of orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    age: int
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    age: int
    email: str

    class Config:
        from_attributes = True  # instead of orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
