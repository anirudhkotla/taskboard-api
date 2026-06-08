from typing import Optional
from pydantic import BaseModel

class ProjectBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class ProjectCreate(ProjectBase):
    title: str
    tenant_id: int

class ProjectUpdate(ProjectBase):
    pass

class ProjectInDBBase(ProjectBase):
    id: int
    tenant_id: int

    class Config:
        from_attributes = True

class Project(ProjectInDBBase):
    pass
