from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.requirement_model import RequirementModel
from core.deps import get_session

# Bypass warning SQLModel select
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore
# Fim Bypass


router = APIRouter()


# Post Requirement
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=RequirementModel)
async def post_requirement(requirement: RequirementModel, db: AsyncSession = Depends(get_session)):
    new_requirement = RequirementModel(
        User_ID=requirement.User_ID,
        Hardware_ID=requirement.Hardware_ID,
        Withdrawn_Date=requirement.Withdrawn_Date,
        Return_Date=requirement.Return_Date,
        Status=requirement.Status,
        Observations=requirement.Observations
    )

    db.add(new_requirement)
    await db.commit()

    return new_requirement


# Get Requirements
@router.get('/', response_model=List[RequirementModel])
async def get_requirement(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(RequirementModel)
        result = await session.execute(query)
        requirements: RequirementModel = result.scalars().all()

        return requirements


# Get Requirement
@router.get('/{requirements_id}', response_model=RequirementModel, status_code=status.HTTP_200_OK)
async def get_requirement(requirements_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(RequirementModel).filter(RequirementModel.ID == requirements_id)
        result = await session.execute(query)
        requirement: RequirementModel = result.scalar_one_or_none()

        if requirement:
            return requirement
        else:
            raise HTTPException(detail='Requirement not found',
                                status_code=status.HTTP_404_NOT_FOUND)


# Put Requirement
@router.put('/{requirements_id}', status_code=status.HTTP_202_ACCEPTED, response_model=RequirementModel)
async def put_requirement(requirements_id: int, requirement: RequirementModel, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(RequirementModel).filter(RequirementModel.ID == requirements_id)
        result = await session.execute(query)
        requirement_up: RequirementModel = result.scalar_one_or_none()

        if requirement_up:
            requirement_up.User_ID = requirement.User_ID,
            requirement_up.Hardware_ID = requirement.Hardware_ID,
            requirement_up.Withdrawn_Date = requirement.Withdrawn_Date,
            requirement_up.Return_Date = requirement.Return_Date,
            requirement_up.Status = requirement.Status,
            requirement_up.Observations = requirement.Observations

            await session.commit()

            return requirement_up
        else:
            raise HTTPException(detail='Requirement not found',
                                status_code=status.HTTP_404_NOT_FOUND)


# Delete Requirement
@router.delete('/{requirements_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_requirement(requirements_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(RequirementModel).filter(RequirementModel.ID == requirements_id)
        result = await session.execute(query)
        requirement_del: RequirementModel = result.scalar_one_or_none()

        if requirement_del:
            await session.delete(requirement_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Requirement not found',
                                status_code=status.HTTP_404_NOT_FOUND)
