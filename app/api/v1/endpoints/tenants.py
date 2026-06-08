from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.tenant.Tenant)
def create_tenant(
    *,
    db: Session = Depends(deps.get_db),
    tenant_in: schemas.tenant.TenantCreate,
) -> Any:
    """
    Create new tenant.
    """
    tenant = crud.tenant.get_by_slug(db, slug=tenant_in.slug)
    if tenant:
        raise HTTPException(
            status_code=400,
            detail="The tenant with this slug already exists in the system.",
        )
    tenant = crud.tenant.create(db, obj_in=tenant_in)
    return tenant

@router.get("/", response_model=List[schemas.tenant.Tenant])
def read_tenants(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve tenants.
    """
    tenants = crud.tenant.get_multi(db, skip=skip, limit=limit)
    return tenants
