from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.tenant import Tenant
from app.schemas.tenant import TenantCreate, TenantUpdate

class CRUDTenant:
    def get(self, db: Session, id: int) -> Optional[Tenant]:
        return db.query(Tenant).filter(Tenant.id == id).first()

    def get_by_slug(self, db: Session, slug: str) -> Optional[Tenant]:
        return db.query(Tenant).filter(Tenant.slug == slug).first()

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Tenant]:
        return db.query(Tenant).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: TenantCreate) -> Tenant:
        db_obj = Tenant(
            name=obj_in.name,
            slug=obj_in.slug
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, db_obj: Tenant, obj_in: TenantUpdate) -> Tenant:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in update_data:
            setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> Tenant:
        obj = db.query(Tenant).get(id)
        db.delete(obj)
        db.commit()
        return obj

tenant = CRUDTenant()
