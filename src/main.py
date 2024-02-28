from fastapi import FastAPI
import services as _services 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "welcome to this cool historical events api"}

@app.get("/events")
async def all_events():
    return _services.get_all_events()

