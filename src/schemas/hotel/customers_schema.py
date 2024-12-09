from pydantic import BaseModel
"""
booking_id (Primary Key)
customer_id (Foreign Key referencing Customer)
hotel_id (Foreign Key referencing Hotel)
room_number (Foreign Key referencing Room)
check_in_date
check_out_date
booking_date
status (e.g., confirmed, canceled)
payment_status (e.g., paid, pending)
"""

""" 
class HotelCustomers(BaseModel):
    booking_id: int
    customer_id: int
    hotel_id: int
    room_number: int
    check_in_date: str
    check_out_date: str
    booking_date: str
    status: str
    payment_status: str """
