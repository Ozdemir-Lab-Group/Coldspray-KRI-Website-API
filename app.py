from fastapi import FastAPI, Depends

from auth.jwt_bearer import JWTBearer
from config.config import initiate_database
from routes.admin import router as AdminRouter
from routes.substratePowder import router as SubstratePowderRouter
from routes.repairToolbox import router as repairToolboxRouter
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

token_listener = JWTBearer()


@app.on_event("startup")
async def start_database():
    await initiate_database()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(SubstratePowderRouter, tags=["SubstratePowder"], prefix="/substratePowder")
app.include_router(repairToolboxRouter, tags=["RepairToolbox"], prefix="/repairToolbox")

