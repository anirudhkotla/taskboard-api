from sqlalchemy.orm import Session
from app import crud, schemas
from app.db.session import SessionLocal
from app.core.config import settings

def init_db(db: Session) -> None:
    # Create first tenant
    tenant_in = schemas.tenant.TenantCreate(
        name="Default Tenant",
        slug="default"
    )
    tenant = crud.tenant.get_by_slug(db, slug=tenant_in.slug)
    if not tenant:
        tenant = crud.tenant.create(db, obj_in=tenant_in)

    # Create superuser
    user_in = schemas.user.UserCreate(
        email="admin@taskboard.com",
        password="adminpassword",
        is_superuser=True,
        tenant_id=tenant.id
    )
    user = crud.user.get_by_email(db, email=user_in.email)
    if not user:
        user = crud.user.create(db, obj_in=user_in)

if __name__ == "__main__":
    db = SessionLocal()
    init_db(db)
    print("Initial data created")
