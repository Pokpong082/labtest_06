import json
from fastapi import APIRouter
import datetime

year_api_router = APIRouter()

@year_api_router.get("/service/getage")
async def getyear_test(year : int):
    cerrent_year = 2565
    if year != 0 :
        if year > cerrent_year:
            age = "Value out of Bound"
        else:
            age = cerrent_year - year
    elif year <= 0 :
        age = "Value = 0 or less than"
        
    return {"age": age}

