from fastapi import FastAPI
from app.tasks import schedule_tasks
from app.routers import posts

app = FastAPI(title="datapulse")

app.include_router(posts.router)

@app.on_event("startup")
async def startup_event():
    schedule_tasks()

@app.get("/")
async def read_root():
    return {"message": "Welcome to Datapulse"}

