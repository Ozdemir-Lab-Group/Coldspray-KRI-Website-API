from typing import Optional
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    __tablename__ = "users"

    email: Optional[EmailStr]
