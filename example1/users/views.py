from example1.users.schemas import CreateUser
from fastapi import APIRouter
from example1.users import crud  # интересное решение ?!


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(user: CreateUser):
    return crud.create_user(
        user_in=user
    )  # наименование переменной совсем не обязатьельно как 'user'
