from typing import Optional
from pydantic import BaseModel

class TenantBase(BaseModel):
    name: str
    slug: str

class TenantCreate(TenantBase):
    pass

class TenantUpdate(TenantBase):
    name: Optional[str] = None
    slug: Optional[str] = None

class TenantInDBBase(TenantBase):
    id: int

    class Config:
        from_attributes = True

class Tenant(TenantInDBBase):
    pass
