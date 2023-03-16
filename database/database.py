from typing import List, Union

from beanie import PydanticObjectId

from models.admin import Admin
from models.substratePowder import SubstratePowder

import json



admin_collection = Admin


async def add_admin(new_admin: Admin) -> Admin:
    admin = await new_admin.create()
    return admin


async def get_powders_by_substrate(substrate: str) -> Union[bool, List[SubstratePowder]]:
    powders = await SubstratePowder.find(SubstratePowder.substrateMaterials == substrate).to_list()
    print(powders)

    if powders:
        return powders
    return False


async def get_substrates() -> Union[bool, List[str]]:
    powders = await SubstratePowder.find_all().to_list()
    print(powders)
    if powders:
        return set([powder.substrateMaterials for powder in powders])
    return False



async def instantiate_powder_data() -> bool:
    f = open("/Users/john/Documents/Projects/ColdsprayAPI/initMongo/powder.json")
    new_data = json.load(f)

    for powder in new_data:
        new_powder = SubstratePowder(
            open = powder["open"],
            substrateMaterials = powder["substrateMaterials"],
            powderType = powder["powderType"],
            substrateSupplier = powder["substrateSupplier"],
            powderSupplier = powder["powderSupplier"],
            subtratePrep = powder["subtratePrep"],
            powderSphericity = powder["powderSphericity"],
            powderSize10 = powder["powderSize10"],
            powderSize50 = powder["powderSize50"],
            powderSize90 = powder["powderSize90"],
            bondLayer =  powder["bondLayer"],
            csMachine = powder["csMachine"],
            nozzle = powder["nozzle"],
            gasType =  powder["gasType"],
            gasPressure = powder["gasPressure"],
            gasTemperature =  powder["gasTemperature"],
            tripleLugShear =  powder["tripleLugShear"],
            heatTreated = powder["heatTreated"],
            porosity = powder["porosity"],
            tensileStrength = powder["tensileStrength"],
            elongation = powder["elongation"],
            bondBarTest = powder["bondBarTest"],
            wear = powder["wear"],
            thermalConductivity = powder["thermalConductivity"],
            electricConductivity = powder["electricConductivity"],
            corrosionCharacteristics = powder["corrosionCharacteristics"])
        return_powder = await new_powder.create()
    
    f.close()

    return True
