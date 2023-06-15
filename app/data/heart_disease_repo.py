from app.data.control_system import diagnosis
from app.domain.interface.symptom_repo import SymptomRepository
from app.domain.schema.symptom import SymptomsIn, HeartDiseaseLevel


class HeartDiseaseRepo(SymptomRepository):
    def __init__(self):
        self.diagnosis = diagnosis

    def get_result(self, symptoms: SymptomsIn) -> HeartDiseaseLevel:
        self.diagnosis.input['chest_pain'] = symptoms.chest_pain
        self.diagnosis.input['exercise'] = symptoms.exercise
        self.diagnosis.input['thallium'] = symptoms.thallium
        self.diagnosis.input['sex'] = symptoms.sex
        self.diagnosis.input['age'] = symptoms.age
        self.diagnosis.input['blood_pressure'] = symptoms.blood_pressure
        self.diagnosis.input['blood_sugar'] = symptoms.blood_sugar
        self.diagnosis.input['cholesterol'] = symptoms.cholesterol
        self.diagnosis.input['maximum_heart_rate'] = symptoms.maximum_heart_rate
        self.diagnosis.input['ecg'] = symptoms.ecg
        self.diagnosis.input['old_peak'] = symptoms.old_peak

        self.diagnosis.compute()

        health = self.diagnosis.output['health']
        return HeartDiseaseLevel(level=health)
