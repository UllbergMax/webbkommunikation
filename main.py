from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/rooms")
def get_rooms():
    return [
        {"room_number": "101", "room_type": "Double room", "price": 1200},
        {"room_number": "102", "room_type": "Single room", "price": 900},
        {"room_number": "103", "room_type": "Single room", "price": 900},
    ]

@app.get("/")
def read_root():
    return {"msg": "Väölkommen till vårt hotell!"}

@app.get("/rooms")
def get_rooms():
    return temp_rooms

@app.get("/bookings")
def create_booking():
    # skapa bokningen i databasen, INSERT INTO bookings (room_number, guest_name, check_in_date, check_out_date) VALUES (...)
    return   