from fastapi import FastAPI
from core.config import settings
from api.tasks import router as tasks_router

app = FastAPI(title=settings.APP_NAME)

app.include_router(tasks_router)
