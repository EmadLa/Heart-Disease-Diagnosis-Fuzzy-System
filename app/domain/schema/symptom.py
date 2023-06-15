from pydantic import BaseModel


class SymptomsIn(BaseModel):
    sex: int
    age: int
    maximum_heart_rate: int
    blood_sugar: int
    blood_pressure: int
    cholesterol: int
    thallium: int
    ecg: int
    chest_pain: int
    exercise: int
    old_peak: int


class HeartDiseaseLevel(BaseModel):
    level: int
