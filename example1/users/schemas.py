from pydantic import BaseModel, EmailStr, Field
from typing import Annotated
from fastapi import Path
from annotated_types import MinLen, MaxLen


class CreateUser(BaseModel):
    # username: str = Field(..., min_length=3, max_length=30) # старое решение, можно исопльзовать
    username: Annotated[str, MinLen(3), MaxLen(30)]
    email: EmailStr
