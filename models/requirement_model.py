from typing import Optional

from datetime import datetime

from sqlmodel import Field, SQLModel


class RequirementModel(SQLModel, table=True):
    __tablename__: str = 'tb_requirements'

    ID: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    User_ID: int
    Hardware_ID: int
    Withdrawn_Date: datetime
    Return_Date: datetime
    Status: str
    Observations: str

    class Config:
        arbitrary_types_allowed = True
