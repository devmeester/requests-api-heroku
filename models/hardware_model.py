from typing import Optional

from sqlmodel import Field, SQLModel


class HardwareModel(SQLModel, table=True):
    __tablename__: str = 'tb_hardware'

    ID: Optional[int] = Field(default=None, primary_key=True)
    Description: str
    Manufacturer: str
    Voltage: str
    Serial_Number: str
    Size: int
    Measure_Unity: str
    Hardware_Type: str
    Hardware_Material: str
    Max_Lenght_Reserve: str
    Status: str
