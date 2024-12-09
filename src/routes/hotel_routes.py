from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm import Session

from .. import models
from ..database import get_db
from ..schemas.hotel.hotel_schema import HotelCreate, Hotels
from .. import oauth


router = APIRouter(prefix="/hotels", tags=["Hotels"])  # Tags for swagger


@router.get("/", response_model=List[Hotels])
def read_hotels(
        db: Session = Depends(get_db),
        skip: int = 5,):
    hotels = db.query(models.Hotels).all()
    return hotels


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=Hotels)
def create_hotel(
        payload: HotelCreate,
        db: Session = Depends(get_db),
        user_id: int = Depends(oauth.get_current_user)
):
    print(user_id)
    try:
        db_hotel = models.Hotels(**payload.model_dump())
        db.add(db_hotel)
        db.commit()
        db.refresh(db_hotel)
        return db_hotel
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/get/{hotel_id}", response_model=Hotels)
def read_hotel_by_id(
        hotel_id: int,
        db: Session = Depends(get_db)):
    try:
        hotel = db.query(models.Hotels).filter(models.Hotels.id == hotel_id)
        if not hotel.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Hotel not found")
        return hotel.first()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.patch("/update/{hotel_id}", response_model=Hotels)
def update_hotel(
        hotel_id: int,
        payload: HotelCreate,
        db: Session = Depends(get_db),
        user_id: int = Depends(oauth.get_current_user)):
    try:
        db_hotel = db.query(models.Hotels).filter(models.Hotels.id == hotel_id)
        if not db_hotel.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Hotel not found")
        db_hotel.update(payload.model_dump())
        db.commit()
        return db_hotel.first()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/delete/{hotel_id}")
def delete_hotel(
        hotel_id: int,
        db: Session = Depends(get_db),
        user_id: int = Depends(oauth.get_current_user)):
    try:
        db_hotel = db.query(models.Hotels).filter(models.Hotels.id == hotel_id)
        if not db_hotel.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Hotel not found")
        db.delete(db_hotel.first(), synchronize_session=False)
        db.commit()
        return {"message": "Hotel deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
