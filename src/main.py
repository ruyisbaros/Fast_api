from .database import get_db, engine
from fastapi import FastAPI, status, Response, Depends
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .routes import hotel_routes

app = FastAPI()
get_db()  # run DB connection

models.Base.metadata.create_all(bind=engine)

# CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SET ROUTES
app.include_router(hotel_routes.router)
# app.include_router(userRoutes.router)
# app.include_router(authRoutes.router)
# app.include_router(voteRoutes.router)
