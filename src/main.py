from fastapi import FastAPI, status, Response
from fastapi.params import Body
from .schemas.hotel.hotel_schema import Hotel

app = FastAPI()


@app.get("/hotels")
def get_hotels():
    return {"message": "These are hotels"}


@app.post("/hotels/create")
def create_hotel(payload: Hotel):
    print(payload.model_dump())
    return {"data": payload}


@app.patch("/hotels/{hotel_id}")
def update_hotel(hotel_id: int, payload: Hotel):
    print(f"Updating hotel with id: {hotel_id}")
    print(payload.model_dump())
    return {"data": payload}


@app.delete("/hotels/{hotel_id}")
def delete_hotel(hotel_id: int):
    print(f"Deleting hotel with id: {hotel_id}")
    return {"message": "Hotel deleted successfully"}


@app.get("/hotels/{hotel_id}")
def get_hotel(hotel_id: int):
    print(f"Getting hotel with id: {hotel_id}")
    return {"message": f"Hotel with id: {hotel_id}"}
