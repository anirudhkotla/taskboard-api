from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Project(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text)
    tenant_id = Column(Integer, ForeignKey("tenant.id"), nullable=False)
    
    tenant = relationship("Tenant")
    tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")

class Task(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text)
    status = Column(String, default="todo")
    project_id = Column(Integer, ForeignKey("project.id"), nullable=False)
    tenant_id = Column(Integer, ForeignKey("tenant.id"), nullable=False)
    
    project = relationship("Project", back_populates="tasks")
    tenant = relationship("Tenant")
