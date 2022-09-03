from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.user_model import UserModel
from core.deps import get_session

# Bypass warning SQLModel select
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore
# Fim Bypass


router = APIRouter()


# Post User
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserModel)
async def post_user(user: UserModel, db: AsyncSession = Depends(get_session)):
    new_user = UserModel(
        Cpf=user.Cpf,
        FirstName=user.FirstName,
        MiddleName=user.MiddleName,
        LastName=user.LastName,
        Sector=user.Sector,
        Position=user.Position,
        Email=user.Email,
        TelePhone=user.TelePhone,
        CellPhone=user.CellPhone,
        AddressStreet=user.AddressStreet,
        AddressNumber=user.AddressNumber,
        AddressComplement=user.AddressComplement,
        District=user.District,
        City=user.City,
        State=user.State
    )

    db.add(new_user)
    await db.commit()
    return new_user


# Get ALL Users
@router.get('/', response_model=List[UserModel])
async def get_users(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel)
        result = await session.execute(query)
        users: List[UserModel] = result.scalars().all()

        return users


# Get User BY ID
@router.get('/{users_id}', response_model=UserModel, status_code=status.HTTP_200_OK)
async def get_user(users_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel).filter(UserModel.ID == users_id)
        result = await session.execute(query)
        requirement: UserModel = result.scalar_one_or_none()

        if requirement:
            return requirement
        else:
            raise HTTPException(detail='User not found',
                                status_code=status.HTTP_404_NOT_FOUND)


# Put User
@router.put('/{users_id}', status_code=status.HTTP_202_ACCEPTED, response_model=UserModel)
async def put_user(users_id: int, user: UserModel, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel).filter(UserModel.ID == users_id)
        result = await session.execute(query)
        user_up: UserModel = result.scalar_one_or_none()

        if user_up:
            user_up.User_ID = user.User_ID,
            user_up.Cpf = user_up.Cpf,
            user_up.FirstName = user.FirstName,
            user_up.MiddleName = user.MiddleName,
            user_up.LastName = user.LastName,
            user_up.Sector = user.Sector,
            user_up.Position = user.Position,
            user_up.Email = user.Email,
            user_up.TelePhone = user.TelePhone,
            user_up.CellPhone = user.CellPhone,
            user_up.AddressStreet = user.AddressStreet,
            user_up.AddressNumber = user.AddressNumber,
            user_up.AddressComplement = user.AddressComplement,
            user_up.District = user.District,
            user_up.City = user.City,
            user_up.State = user.State

            await session.commit()

            return user_up
        else:
            raise HTTPException(detail='User not found',
                                status_code=status.HTTP_404_NOT_FOUND)


# Delete User
@router.delete('/{users_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(users_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel).filter(UserModel.ID == users_id)
        result = await session.execute(query)
        user_del: UserModel = result.scalar_one_or_none()

        if user_del:
            await session.delete(user_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='User not found',
                                status_code=status.HTTP_404_NOT_FOUND)
