"""
Создание Create, Read, Update, Delete
"""

from example1.users.schemas import CreateUser


def create_user(user_in: CreateUser) -> dict:
    user = user_in.model_dump()
    return {
        "success": True,
        "user": user,
    }
