from fastapi import APIRouter, HTTPException

from models.task import Task, TaskOut

router = APIRouter(prefix="/tasks", tags=["tasks"])

tasks_db = {}
next_id = 1


@router.get("/", response_model=list[TaskOut])
def get_tasks():
    return list(tasks_db.values())


@router.post("/", response_model=TaskOut, status_code=201)
def create_task(task: Task):
    global next_id
    new_task = {"id": next_id, **task.model_dump()}
    tasks_db[next_id] = new_task
    next_id += 1
    return new_task


@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int):
    task = tasks_db.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task
