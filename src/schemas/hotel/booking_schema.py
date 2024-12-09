from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from ..hotel.hotel_schema import Hotels
from ..users.user_schema import UserOut


class Booking_Base(BaseModel):
    customer_id: int
    hotel_id: int
    check_in_date: datetime
    check_out_date: datetime


class BookingOut(BaseModel):
    id: int
    created_at: datetime
    # we added this parameter in models as relationships
    hotel: Optional[Hotels] = None
    # we added this parameter in models as relationships
    customer: Optional[UserOut] = None

    class Config:
        from_attributes = True
