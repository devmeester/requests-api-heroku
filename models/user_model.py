from typing import Optional
from sqlmodel import Field, SQLModel


class UserModel(SQLModel, table=True):
    __tablename__: str = 'tb_users'

    ID: Optional[int] = Field(default=None, primary_key=True)
    Cpf: str
    FirstName: str
    MiddleName: Optional[str]
    LastName: str
    Sector: Optional[str]
    Position: Optional[str]
    Email: Optional[str]
    TelePhone: Optional[str]
    CellPhone: Optional[str]
    AddressStreet: Optional[str]
    AddressNumber: Optional[str]
    AddressComplement: Optional[str]
    District: Optional[str]
    City: Optional[str]
    State: Optional[str]