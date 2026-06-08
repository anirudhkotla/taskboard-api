from typing import Optional
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = "todo"

class TaskCreate(TaskBase):
    title: str
    project_id: int
    tenant_id: int

class TaskUpdate(TaskBase):
    pass

class TaskInDBBase(TaskBase):
    id: int
    project_id: int
    tenant_id: int

    class Config:
        from_attributes = True

class Task(TaskInDBBase):
    pass
