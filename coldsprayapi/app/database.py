from typing import Optional, List
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("MONGODB_URL")
db = client.college


@as_declarative()
class Base:

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
