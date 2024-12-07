from pydantic import BaseModel, EmailStr
from datetime import datetime

##### User ########


class UserCreate(BaseModel):
    email: EmailStr
    password: str

    def __getitem__(self, key):
        return self.__dict__[key]


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str
