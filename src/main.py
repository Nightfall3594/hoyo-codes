from fastapi import FastAPI

from src.scraper import Scraper

app = FastAPI()

@app.get("/codes/star-rail")
def get_codes():
    return {"codes" : Scraper.get_valid_codes()}