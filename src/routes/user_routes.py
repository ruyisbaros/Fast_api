from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from .. import models
from ..database import get_db
from ..schemas.users.user_schema import UserCreate, UserOut, Token
from ..utils import hash_paswords, verify_password
from ..oauth import create_access_token

router = APIRouter(prefix="/users", tags=["Users"])  # Tags for swagger


@router.post("/auth/register", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_user(
        payload: UserCreate,
        db: Session = Depends(get_db)):
    """Create a new user."""
    # print(payload.email)
    try:
        is_email_exist = db.query(models.User).filter(
            models.User.email == payload.email).first()
        if is_email_exist:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        # hash the password
        payload.password = hash_paswords(payload.password)
        new_user = models.User(**payload.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/auth/login", response_model=Token)
def login_user(
        payload: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)):
    """Login an existing user."""
    try:
        # Check if user exists
        loggedIn = (
            db.query(models.User)
            # OAuth keeps email as username and accepts credentials as form-data not a body
            .filter(models.User.email == payload.username)
            .first()
        )
        # print(loggedIn.password)
        if not loggedIn:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
            )
        # Check if password is correct
        password_match = verify_password(payload.password, loggedIn.password)

        if not password_match:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
            )
         # Create access token
        access_token = create_access_token(
            data={"user_id": loggedIn.id, "email": loggedIn.email}
        )

        return {
            "token_type": "bearer",
            "access_token": access_token,
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/all", response_model=List[UserOut])
def read_users(
        db: Session = Depends(get_db),
        skip: int = 0):
    """Read all users."""
    # users = db.query(models.User).offset(skip).limit(5).all()
    users = db.query(models.User).offset(skip).all()
    return users


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserOut)
def read_user(
        user_id: int,
        db: Session = Depends(get_db)):
    """Read a single user."""
    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserOut)
def update_user(
        user_id: int,
        payload: UserCreate,
        db: Session = Depends(get_db)):
    """Update a user."""
    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        user.update(payload.model_dump())
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
        user_id: int,
        db: Session = Depends(get_db)):
    """Delete a user."""
    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        db.delete(user)
        db.commit()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
