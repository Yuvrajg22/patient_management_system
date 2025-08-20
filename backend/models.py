from pydantic import BaseModel
from typing import Optional

class Patient(BaseModel):
    id: str
    name: str
    city: str
    age: int
    gender: str
    height: float
    weight: float
    bmi: float
    verdict: str

class PatientCreate(BaseModel):
    name: str
    city: str
    age: int
    gender: str
    height: float
    weight: float

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    height: Optional[float] = None
    weight: Optional[float] = None