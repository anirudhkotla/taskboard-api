# TaskBoard API

Multi-tenant backend API for TaskBoard project.

## Stack
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic

## Getting Started

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables (DATABASE_URL, SECRET_KEY)
4. Run migrations: `alembic upgrade head`
5. Start the server: `uvicorn app.main:app --reload`
