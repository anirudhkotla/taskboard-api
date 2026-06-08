from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.project.Project])
def read_projects(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.user.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve projects for the current tenant.
    """
    projects = crud.project.get_multi_by_tenant(
        db, tenant_id=current_user.tenant_id, skip=skip, limit=limit
    )
    return projects

@router.post("/", response_model=schemas.project.Project)
def create_project(
    *,
    db: Session = Depends(deps.get_db),
    project_in: schemas.project.ProjectCreate,
    current_user: models.user.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new project.
    """
    project = crud.project.create_with_tenant(
        db, obj_in=project_in, tenant_id=current_user.tenant_id
    )
    return project
