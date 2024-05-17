from fastapi import APIRouter, Depends
from services.UserService import UserService

UsersRouter = APIRouter(
    prefix="/users", tags=["users"]
)

@UsersRouter.get("/")
def list(userService: UserService = Depends()):
    return userService.list()

@UsersRouter.get("/{id}")
def get(
        id: int,
        userService: UserService = Depends()
    ):
    return userService.get(id)

@UsersRouter.get("/{id}/name")
def get(
        id: int,
        userService: UserService = Depends()
    ):
    return userService.getNameByUserId(id)

@UsersRouter.get("/{id}/subscription")
def get(
        id: int,
        userService: UserService = Depends()
    ):
    return userService.getSubscriptionByUserId(id)