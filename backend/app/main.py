from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Interview Coach")

app.include_router(router)