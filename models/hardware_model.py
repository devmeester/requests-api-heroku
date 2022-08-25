from typing import Optional

from sqlmodel import Field, SQLModel


class HardwareModel(SQLModel, table=True):
    __tablename__: str = 'tb_hardware'

    ID: Optional[int] = Field(default=None, primary_key=True)
    Serial_Number: str
    Name: str
    Description: Optional[str]
    Cost: float
    Status: bool
