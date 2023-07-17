from fastapi import FastAPI
import uvicorn
from models import Data
from database_conn import init_db, create_db, db_do


app = FastAPI()


@app.on_event('startup')
async def startup():
    create_db()
    await init_db()


@app.get("/")
async def root():
    return {"msg": "app is active"}


@app.post("/load", tags=["load_tarif"])
async def load_tarif(json_file: dict):
    """TODO: load tarif to database, parse"""
    for key in json_file.keys():
        date: str = key
        print(json_file[date])
        for i in range(len(json_file[date])):
            cargo_type: str = json_file[date][i].get("cargo_type", "Cargo_type is not found")
            rate: float = json_file[date][i].get("rate", "Rate is not found")
            db_do(f"""INSERT INTO data ("date","cargo_type","rate") values('{date}','{cargo_type}','{rate}')""")
    return {"msg": "Your tarif was loaded"}


@app.get("/get_cost", tags=["get_cost"])
async def get_cost(date:str, cargo_type:str, declared_cost:int):
    """TODO: find in database, return (declared * rate) """
    data = db_do(f"""SELECT rate FROM data WHERE date = '{date}' and cargo_type = '{cargo_type}' """)[0][0]
    res = float(data)*declared_cost
    return {f"Your {cargo_type} {declared_cost} is ": res}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)