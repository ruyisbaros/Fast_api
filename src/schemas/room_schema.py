from typing import List
from pydantic import BaseModel

"""
id	INTEGER (Primary Key)	Unique identifier for each room.
hotel_id	INTEGER (Foreign Key)	Links to the id in the Hotels table.
room_number	VARCHAR	Unique room number within the hotel.
type	VARCHAR	Type of room (e.g., Single, Double, Suite).
price_per_night	DECIMAL	Cost per night for the room.
availability	BOOLEAN	Indicates if the room is available.
description	TEXT	Additional details about the room.
photo_url	VARCHAR	Link to a photo of the room.
"""


class Room(BaseModel):
    id: int
    hotel_id: int
    room_number: int
    type: str
    price_per_night: float
    availability: bool
    description: str
    photo_url: List[str]
