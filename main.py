
from fastapi import FastAPI

from configs.Environment import get_environment_variables
from metadata.Tags import Tags
from routers.v1.UsersRouter import UsersRouter

env = get_environment_variables()

app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
    openapi_tags=Tags,
)

app.include_router(UsersRouter)

@app.get("/")
async def root():
    return {
        "message": "Welcome!"
    }
