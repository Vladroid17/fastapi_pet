from fastapi import FastAPI
from src.schemas.tasks import TaskSchema
from contextlib import asynccontextmanager

# from src.db.database import create_tables, delete_tables
from src.api.tasks import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_tables()
    print("tables deleted")
    # await create_tables()
    print("app is starting up")
    yield
    print("app is shutting down")
    
app = FastAPI(lifespan=lifespan)
app.include_router(task_router)


