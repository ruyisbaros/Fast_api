from typing import List
from pydantic import BaseModel


class Hotel(BaseModel):
    name: str
    address: str
    city: str
    price: float
    stars: int
    accommodation: str
    amenities: List[str]
    email: str
    phone: str
