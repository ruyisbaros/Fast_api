from .database import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY, Float, Boolean, DateTime
from sqlalchemy.sql.sqltypes import TIMESTAMP, DATETIME
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))


class Hotels(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, index=True, nullable=False, unique=True)
    address = Column(String, nullable=False)
    city = Column(String, index=True, nullable=False)
    stars = Column(Integer)
    lowest_price = Column(Float, index=True)
    accommodation = Column(String, index=True)
    amenities = Column(ARRAY(String))
    email = Column(String,  nullable=False)
    phone = Column(String, )
    photo_url = Column(ARRAY(String), index=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


class Bookings(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    hotel_id = Column(Integer, ForeignKey("hotels.id"),
                      index=True, nullable=False)
    customer_id = Column(Integer, ForeignKey(
        "users.id", ondelete='CASCADE'), nullable=False)
    check_in_date = Column(DateTime, nullable=False)
    check_out_date = Column(DateTime, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    hotel = relationship("Hotels")
    customer = relationship("User")


""" class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), nullable=False)
    room_number = Column(String, index=True, nullable=False)
    type = Column(String, nullable=False)
    price_per_night = Column(Float, nullable=False)
    availability = Column(Boolean, nullable=False)
    description = Column(String)
    photo_url = Column(ARRAY(String), index=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
 """
""" 
class HotelCustomer(Base):
    __tablename__ = "hotel_customers"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), nullable=False)
    booking_id = Column(Integer, ForeignKey("bookings.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    check_in_date = Column(TIMESTAMP(timezone=True), nullable=False)
    check_out_date = Column(TIMESTAMP(timezone=True), nullable=False)
    booking_date = Column(TIMESTAMP(timezone=True),
                          server_default=text('now()'), nullable=False)
    status = Column(String, nullable=False)
    payment_status = Column(Boolean, nullable=False, server_default="False")
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()')) """
