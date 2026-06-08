from typing import List
from sqlalchemy.orm import Session
from app.models.project_task import Task
from app.schemas.task import TaskCreate, TaskUpdate

class CRUDTask:
    def get_multi_by_project(self, db: Session, *, project_id: int, tenant_id: int, skip: int = 0, limit: int = 100) -> List[Task]:
        return db.query(Task).filter(Task.project_id == project_id, Task.tenant_id == tenant_id).offset(skip).limit(limit).all()

    def create_with_project(self, db: Session, *, obj_in: TaskCreate, tenant_id: int) -> Task:
        db_obj = Task(
            title=obj_in.title,
            description=obj_in.description,
            status=obj_in.status,
            project_id=obj_in.project_id,
            tenant_id=tenant_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

task = CRUDTask()
