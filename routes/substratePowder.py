from fastapi import APIRouter, Body

from database.database import *
from models.substratePowder import *

router = APIRouter()

@router.post("/instantiate", response_description="Populate JSON data ")
async def instantiate_powder():
    is_instantiated = await instantiate_powder_data()
    if is_instantiated:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Student data retrieved successfully",
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Error in instantiating powder data",
    }



@router.get("/{substrate}", response_description="Get all substrate powders")
async def get_substrate_powders_combinations(substrate: str):
    substratePowders = await get_powders_by_substrate(substrate)
    if substratePowders:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Substrate powder data retrieved successfully",
            "data": substratePowders
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Student don't exist",
    }

@router.get("/substrates/getAll", response_description="Get all substrates")
async def get_all_substrates():
    substratePowders = await get_substrates()
    if substratePowders:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Substrate powder data retrieved successfully",
            "data": substratePowders
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Powders don't exist",
    }


