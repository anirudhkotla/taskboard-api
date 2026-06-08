import modal

# Define the container image with all necessary dependencies
image = (
    modal.Image.debian_slim()
    .pip_install_from_requirements("requirements.txt")
)

# Initialize the Modal App
app = modal.App("taskboard-api")

@app.function(
    image=image,
    # Mount the 'app' directory to the remote container
    mounts=[modal.Mount.from_local_dir("app", remote_path="/root/app")],
    # Reference a Modal Secret for environment variables (DATABASE_URL, SECRET_KEY, etc.)
    secrets=[modal.Secret.from_name("taskboard-secrets")]
)
@modal.asgi_app()
def api():
    """
    Entrypoint for the FastAPI application on Modal.
    This function imports the FastAPI app instance and returns it to be served as an ASGI app.
    """
    from app.main import app as fastapi_app
    return fastapi_app

if __name__ == "__main__":
    app.serve()
