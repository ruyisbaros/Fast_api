from pydantic import BaseModel

"""
id	INTEGER (Primary Key)	Unique identifier for each passenger.
name	VARCHAR	Full name of the passenger.
email	VARCHAR	Contact email.
phone	VARCHAR	Contact number.
passport_number	VARCHAR	Passport number of the passenger.
"""


class Passenger(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    passport_number: str
