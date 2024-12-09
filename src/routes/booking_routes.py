from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm import Session

from .. import models
from ..database import get_db
from ..schemas.hotel.booking_schema import Booking_Base, BookingOut
from .. import oauth


router = APIRouter(prefix="/bookings", tags=["Bookings"])  # Tags for swagger


@router.get("/", response_model=List[BookingOut])
def read_bookings(
        db: Session = Depends(get_db),
        skip: int = 5,):
    bookings = db.query(models.Bookings).all()
    return bookings


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=BookingOut)
def create_booking(
        payload: Booking_Base,
        db: Session = Depends(get_db)):
    new_booking = models.Bookings(**payload.model_dump())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking


@router.get("/get/{booking_id}", response_model=BookingOut)
def read_booking_by_id(
        booking_id: int,
        db: Session = Depends(get_db)):
    booking = db.query(models.Bookings).filter(
        models.Bookings.id == booking_id).first()
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")
    return booking


@router.patch("/update/{booking_id}", response_model=BookingOut)
def update_booking(
        booking_id: int,
        payload: Booking_Base,
        db: Session = Depends(get_db)):
    booking = db.query(models.Bookings).filter(
        models.Bookings.id == booking_id).first()
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")
    booking.update(payload.dict())
    db.commit()
    db.refresh(booking)
    return booking
