from pydantic import BaseModel


class Run(BaseModel):
    id: int
    timeCreated: date
