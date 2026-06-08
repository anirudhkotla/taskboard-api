from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.task.Task])
def read_tasks(
    project_id: int,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.user.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve tasks for a specific project.
    """
    tasks = crud.task.get_multi_by_project(
        db, project_id=project_id, tenant_id=current_user.tenant_id, skip=skip, limit=limit
    )
    return tasks

@router.post("/", response_model=schemas.task.Task)
def create_task(
    *,
    db: Session = Depends(deps.get_db),
    task_in: schemas.task.TaskCreate,
    current_user: models.user.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new task.
    """
    task = crud.task.create_with_project(
        db, obj_in=task_in, tenant_id=current_user.tenant_id
    )
    return task
