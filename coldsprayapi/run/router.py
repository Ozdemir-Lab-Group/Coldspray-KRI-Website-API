from fastapi import APIRouter

router = APIRouter()

@router.get('runs/{username}', tags=["runs"])
async def getUserRuns(username: str):
    return {"username": username}