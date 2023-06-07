
from typing import List

from fastapi import FastAPI, APIRouter

from orders.schemas import Place
from orders.router import router as order_router

app = FastAPI()

place_router = APIRouter(
    prefix = "/place",
    tags =["Place"]
)
app.include_router(order_router)
app.include_router(place_router)


places = [
    {"place_id": 1, "name": "Golden cafe", "address": "Pyshkina 23", "phone": "+375447890929", "category": "cafe",
     "tables": ""},
    {"place_id": 2, "name": "Terra", "address": "Surganovo 12", "phone": "+375447890119", "category": "cafe",
     "tables": ""},
    {"place_id": 3, "name": "BBJ", "address": "Grushevka 91", "phone": "+375447890009", "category": "bar",
     "tables": ""},
    {"place_id": 4, "name": "Butterbro", "address": "Surganovo 88", "phone": "+375447890900", "category": "restaurant",
     "tables": [
         {"table_id": 1,
          "waiter": {
              "waiter_id": 1, "name": "John", "last_name": "Peters"
          },
          "booking_time_table": [
              {"start_armor": "", "end_armor": "2023-05-31T12:30:00"},
              {"start_armor": "2023-05-31T13:00:00", "end_armor": "2023-05-31T15:00:00"},
              {"start_armor": "2023-05-31T19:00:00", "end_armor": "2023-05-31T22:00:00"},
          ]}
     ]},

]





    # @validator('address')
    # def name_must_contain_space(cls,address):
    #     street,number_house = address.split()
    #     if ' ' not in address and not number_house.isdigit():
    #         raise ValueError('must contain a space and number_house must be integer')
    #     return address
    # @validator('address')
    # def name_must_contain_space(cls, v):
    #     if ' ' not in v:
    #         raise ValueError('must contain a space')
    #     return v.title()


@place_router.get("/places")
async def get_places():
    return {"places": places}


@place_router.get("/places/{place_id}")
async def get_place(place_id: int):
    establishments = [est for est in places if est["place_id"] == place_id]
    return {"place": establishments}

@place_router.post("/add_place")
async def post_place(place: List[Place]):
    places.append(place)
    return {"places": places}
