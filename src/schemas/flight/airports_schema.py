from pydantic import BaseModel

"""
id	INTEGER (Primary Key)	Unique identifier for each airport.
code	VARCHAR	Airport code (e.g., LAX, JFK).
name	VARCHAR	Full name of the airport.
city	VARCHAR	City where the airport is located.
country	VARCHAR	Country where the airport is located.
"""


class Airport(BaseModel):
    id: int
    code: str
    name: str
    city: str
    country: str
