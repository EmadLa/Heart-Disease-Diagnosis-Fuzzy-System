from ..interface.symptom_repo import SymptomRepository
from ..schema.symptom import SymptomsIn, HeartDiseaseLevel


class SymptomUC:

    def __init__(self, repository: SymptomRepository) -> None:
        self._repo = repository

    def get_result(self, symptoms: SymptomsIn) -> HeartDiseaseLevel:
        return self._repo.get_result(symptoms)
