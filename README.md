# TaskBoard API

Multi-tenant backend API for task management.

## Deployment on Modal.com

This project is configured for deployment on [Modal](https://modal.com).

### Prerequisites

1.  **Modal Account**: Sign up at [modal.com](https://modal.com).
2.  **Modal CLI**: Install the Modal CLI locally:
    ```bash
    pip install modal
    ```
3.  **Authentication**: Authenticate your local environment:
    ```bash
    modal setup
    ```

### Configuration (Secrets)

The application requires several environment variables for database connection and security. You should create a Modal Secret named `taskboard-secrets` in your Modal dashboard or via CLI.

Required keys in `taskboard-secrets`:
- `DATABASE_URL`: Your PostgreSQL connection string (e.g., Supabase or RDS).
- `SECRET_KEY`: A long random string for JWT signing.
- `PROJECT_NAME`: (Optional) Defaults to "TaskBoard".

To create the secret via CLI:
```bash
modal secret create taskboard-secrets DATABASE_URL=your_url SECRET_KEY=your_key
```

### Deployment Commands

To deploy the API as a persistent web endpoint:
```bash
modal deploy modal_app.py
```

To run the API in "serve" mode (hot-reloading for development):
```bash
modal serve modal_app.py
```

## Local Development

1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the app locally:
    ```bash
    uvicorn app.main:app --reload
    ```
