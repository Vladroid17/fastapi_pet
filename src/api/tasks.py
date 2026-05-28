from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.api.dependencies import tasks_service
from src.repositories.tasks import TasksRepository
from typing import Annotated
from src.db.database import get_async_session
from src.models.tasks import Tasks
from src.schemas.tasks import TaskSchemaAdd
from src.services.tasks import TasksService 


   
router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)   
   
# @router.post("")
# async def add_task(
#     task: TaskSchemaAdd,
#     tasks_service: Annotated[TasksService, Depends(tasks_service)],
# ):
#     task_id = await tasks_service.add_task(task)
#     return {"task_id": task_id}


@router.post("")
async def add_tasks(
    task: TaskSchemaAdd,
    tasks_service: Annotated[TasksService, Depends(tasks_service)],
):
    task_id = await tasks_service.add_task(task)
    return {"task_id": task_id}

@router.get("")
async def get_tasks(session: Annotated[AsyncSession, Depends(get_async_session)]):
    stmt = select(Tasks)
    res = await session.execute(stmt)
    res = [row[0].to_read_model() for row in res.all()]
    return res