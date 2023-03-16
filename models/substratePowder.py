from beanie import Document
from pydantic import BaseModel, EmailStr




class SubstratePowder(Document):
    _id: str
    open: bool
    substrateMaterials: str
    powderType: str
    substrateSupplier: str
    powderSupplier: str
    subtratePrep: str
    powderSphericity: str
    powderSize10: str
    powderSize50: str
    powderSize90: str
    bondLayer: str
    csMachine: str
    nozzle: str
    gasType: str
    gasPressure: str
    gasTemperature: str
    heatTreated: str
    porosity: str
    tensileStrength: str
    elongation: str
    tripleLugShear: str
    bondBarTest: str
    wear: str
    thermalConductivity: str
    electricConductivity: str
    corrosionCharacteristics: str

    class Collection:
        name = "substratePowder"

    class Config:
        schema_extra = {
            "example": {
                "_id": 1,
                "open": True,
                "substrateMaterials": "Al-6061",
                "powderType": "Al-6061",
                "substrateSupplier": "Mcmaster",
                "powderSupplier": "Solvus",
                "subtratePrep": "Wire brush, Soap",
                "powderSphericity": 1,
                "PowderSize10": 5,
                "powderSize50": 43,
                "powderSize90": 60,
                "bondLayer": "Al-6061, 30 deg",
                "csMachine": "VRC Gen-III",
                "nozzle": "VRC0058",
                "gasType": "N2",
                "gasPressure": "600 KPa",
                "gasTemperature": "400 C",
                "heatTreated": "Annealed",
                "porosity": 0.25,
                "tensileStrength": "40,230 Pa",
                "elongation": 0.2,
                "tripleLugShear": "",
                "bondBarTest": "Glue failure",
                "wear": "800 revs",
                "thermalConductivity": "",
                "electricConductivity": "",
                "corrosionCharacteristics": ""
            }
        }


