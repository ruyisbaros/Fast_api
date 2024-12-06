from fastapi import FastAPI
from fastapi.params import Body


app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, Worlddddd!"}


@app.get("/hotels")
def get_hotels():
    return {"message": "These are hotels"}


@app.post("/hotels/create")
def create_hotel(payload: dict = Body(...)):
    print(payload)
    return {"data": payload}
