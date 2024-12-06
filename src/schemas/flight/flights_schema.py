from pydantic import BaseModel

"""
id	INTEGER (Primary Key)	Unique identifier for each flight.
flight_number	VARCHAR	Flight number (e.g., AA123).
departure_airport_id	INTEGER (Foreign Key)	Links to id in Airports.
arrival_airport_id	INTEGER (Foreign Key)	Links to id in Airports.
departure_time	DATETIME	Scheduled departure time.
arrival_time	DATETIME	Scheduled arrival time.
price	DECIMAL	Ticket price for the flight.
capacity	INTEGER	Number of available seats.
status	VARCHAR	Flight status (e.g., Scheduled, Delayed).

"""


class Flight(BaseModel):
    id: int
    flight_number: str
    departure_airport_id: int
    arrival_airport_id: int
    departure_time: str
    arrival_time: str
    price: float
    capacity: int
    status: str
