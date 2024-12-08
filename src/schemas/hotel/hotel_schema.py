from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class Hotels_Base(BaseModel):
    name: str
    address: str
    city: str
    stars: int
    lowest_price: float
    amenities: List[str]
    accommodation: str
    email: str
    phone: str
    photo_url: List[str] = []

    class Config:
        from_attributes = True


class HotelCreate(Hotels_Base):
    pass


class Hotels(Hotels_Base):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
