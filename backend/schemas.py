from pydantic import BaseModel
from typing import Optional

class PatientBase(BaseModel):
    name: str
    city: str
    age: int
    gender: str
    height: float
    weight: float
    bmi: float
    verdict: str

class PatientCreate(PatientBase):
    pass

class PatientUpdate(PatientBase):
    name: Optional[str] = None
    city: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    bmi: Optional[float] = None
    verdict: Optional[str] = None

class Patient(PatientBase):
    id: str

    class Config:
        orm_mode = True