from app.data.heart_disease_repo import HeartDiseaseRepo
from app.domain.usecase.symptom_uc import SymptomUC


def get_symptom_repo():
    return HeartDiseaseRepo()


def get_symptom_uc():
    return SymptomUC(get_symptom_repo())
