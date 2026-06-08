from typing import List
from sqlalchemy.orm import Session
from app.models.project_task import Project
from app.schemas.project import ProjectCreate, ProjectUpdate

class CRUDProject:
    def get_multi_by_tenant(self, db: Session, *, tenant_id: int, skip: int = 0, limit: int = 100) -> List[Project]:
        return db.query(Project).filter(Project.tenant_id == tenant_id).offset(skip).limit(limit).all()

    def create_with_tenant(self, db: Session, *, obj_in: ProjectCreate, tenant_id: int) -> Project:
        db_obj = Project(
            title=obj_in.title,
            description=obj_in.description,
            tenant_id=tenant_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

project = CRUDProject()
