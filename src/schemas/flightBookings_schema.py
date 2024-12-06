from pydantic import BaseModel

"""
id	INTEGER (Primary Key)	Unique identifier for each booking.
flight_id	INTEGER (Foreign Key)	Links to id in Flights.
passenger_id	INTEGER (Foreign Key)	Links to id in Passengers.
booking_date	DATETIME	Date and time of booking.
seat_number	VARCHAR	Assigned seat number.
price_paid	DECIMAL	Price paid for the ticket.
"""


class Booking(BaseModel):
    id: int
    flight_id: int
    passenger_id: int
    booking_date: str
    seat_number: str
    price_paid: float
