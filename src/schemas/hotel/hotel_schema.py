from typing import List, Optional
from pydantic import BaseModel


class Hotel(BaseModel):
    name: str
    address: str
    city: str
    stars: int
    lowest_price: float
    accommodation: str
    amenities: List[str]
    email: str
    phone: str
    photo_url: Optional[List[str]] = []
