from fastapi import APIRouter
from app.api.v1.endpoints import login, projects, tasks, tenants

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(tenants.router, prefix="/tenants", tags=["tenants"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
