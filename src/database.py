import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from .models.hotel_model import Hotel


POSTGRES_USERNAME = os.getenv('POSTGRES_USERNAME')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')

DATABASE_URL = f"postgresql://{POSTGRES_USERNAME}:{
    POSTGRES_PASSWORD}@localhost/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# POSTGRES DB CONNECT IF WE WORK WITH VANILLA SQL
""" while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database=POSTGRES_DB,
            user=POSTGRES_USERNAME,
            password=POSTGRES_PASSWORD,
            cursor_factory=RealDictCursor,
        )
        cursor = conn.cursor()
        print("Database connection established successfully")
        break

    except (Exception, psycopg2.DatabaseError) as e:
        print("Error with connecting to database")
        print("Error: %s" % e)
        time.sleep(2) """
