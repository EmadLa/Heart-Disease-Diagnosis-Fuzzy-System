from abc import ABC, abstractmethod

from ..schema.symptom import SymptomsIn, HeartDiseaseLevel


class SymptomRepository(ABC):

    @abstractmethod
    def get_result(self, symptoms: SymptomsIn) -> HeartDiseaseLevel:
        pass
