from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.hardware_model import HardwareModel
from core.deps import get_session

# Bypass warning SQLModel select
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore
# Fim Bypass


router = APIRouter()


# Post Hardware
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=HardwareModel)
async def post_hardware(hardware: HardwareModel, db: AsyncSession = Depends(get_session)):
    new_hardware = HardwareModel(
        Description=hardware.Description,
        Manufacturer=hardware.Manufacturer,
        Voltage=hardware.Voltage,
        Serial_Number=hardware.Serial_Number,
        Size=hardware.Size,
        Measure_Unity=hardware.Measure_Unity,
        Hardware_Type=hardware.Hardware_Type,
        Hardware_Material=hardware.Hardware_Material,
        Max_Lenght_Reserve=hardware.Max_Lenght_Reserve,
        Status=hardware.Status
    )

    db.add(new_hardware)
    await db.commit()

    return new_hardware


# Get ALL Hardwares
@router.get('/', response_model=List[HardwareModel])
async def get_hardware(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(HardwareModel)
        result = await session.execute(query)
        hardwares: HardwareModel = result.scalars().all()

        return hardwares


# Get Hardware BY ID
@router.get('/{hardware_id}', response_model=HardwareModel, status_code=status.HTTP_200_OK)
async def get_hardware(hardware_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(HardwareModel).filter(HardwareModel.ID == hardware_id)
        result = await session.execute(query)
        hardware: HardwareModel = result.scalar_one_or_none()

        if hardware:
            return hardware
        else:
            raise HTTPException(detail='Hardware not found',
                                status_code=status.HTTP_404_NOT_FOUND)


# Put Hardware
@router.put('/{hardware_id}', status_code=status.HTTP_202_ACCEPTED, response_model=HardwareModel)
async def put_hardware(hardware_id: int, hardware: HardwareModel, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(HardwareModel).filter(HardwareModel.ID == hardware_id)
        result = await session.execute(query)
        hardware_up: HardwareModel = result.scalar_one_or_none()

        if hardware_up:
            hardware_up.User_ID = hardware.User_ID,
            hardware_up.Description = hardware.Description,
            hardware_up.Manufacturer = hardware.Manufacturer,
            hardware_up.Voltage = hardware.Voltage,
            hardware_up.Serial_Number = hardware.Serial_Number,
            hardware_up.Size = hardware.Size,
            hardware_up.Measure_Unity = hardware.Measure_Unity,
            hardware_up.Hardware_Type = hardware.Hardware_Type,
            hardware_up.Hardware_Material = hardware.Hardware_Material,
            hardware_up.Max_Lenght_Reserve = hardware.Max_Lenght_Reserve,
            hardware_up.Status = hardware.Status

            await session.commit()

            return hardware_up
        else:
            raise HTTPException(detail='Hardware not found',
                                status_code=status.HTTP_404_NOT_FOUND)


# Delete Hardware
@router.delete('/{hardware_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_harware(hardware_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(HardwareModel).filter(HardwareModel.ID == hardware_id)
        result = await session.execute(query)
        hardware_del: HardwareModel = result.scalar_one_or_none()

        if hardware_del:
            await session.delete(hardware_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Hardware not found',
                                status_code=status.HTTP_404_NOT_FOUND)
