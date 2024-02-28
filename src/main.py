from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "welcome to this cool historical events api"}