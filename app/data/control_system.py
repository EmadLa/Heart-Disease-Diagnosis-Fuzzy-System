import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Categorical
chest_pain = ctrl.Antecedent(np.arange(0.9, 4.1, 0.00001), 'chest_pain')
exercise = ctrl.Antecedent(np.arange(-0.1, 1.1, 0.00001), 'exercise')
thallium = ctrl.Antecedent(np.arange(2.9, 7.1, 0.00001), 'thallium')
sex = ctrl.Antecedent(np.arange(-0.1, 1.1, 0.00001), 'sex')

# Fuzzy
age = ctrl.Antecedent(np.arange(0, 101, 1), 'age')
blood_pressure = ctrl.Antecedent(np.arange(0, 351, 1), 'blood_pressure')
blood_sugar = ctrl.Antecedent(np.arange(0, 201, 1), 'blood_sugar')
cholesterol = ctrl.Antecedent(np.arange(0, 601, 1), 'cholesterol')
maximum_heart_rate = ctrl.Antecedent(np.arange(0, 601, 1), 'maximum_heart_rate')
ecg = ctrl.Antecedent(np.arange(-0.5, 2.6, 0.1), 'ecg')
old_peak = ctrl.Antecedent(np.arange(0, 10.1, 0.1), 'old_peak')

# Consequent
health = ctrl.Consequent(np.arange(0, 4.01, 0.01), 'health')

chest_pain['typical_anginal'] = fuzz.gaussmf(chest_pain.universe, 1, 0.00001)
chest_pain['atypical_anginal'] = fuzz.gaussmf(chest_pain.universe, 2, 0.00001)
chest_pain['non_aginal_pain'] = fuzz.gaussmf(chest_pain.universe, 3, 0.00001)
chest_pain['asymptomatic'] = fuzz.gaussmf(chest_pain.universe, 4, 0.00001)

age['young'] = fuzz.trapmf(age.universe, [0, 0, 29, 38])
age['mild'] = fuzz.trimf(age.universe, [33, 38, 45])
age['old'] = fuzz.trimf(age.universe, [40, 48, 58])
age['very_old'] = fuzz.trapmf(age.universe, [52, 60, 100, 100])

blood_pressure['low'] = fuzz.trapmf(blood_pressure.universe, [0, 0, 111, 134])
blood_pressure['medium'] = fuzz.trimf(blood_pressure.universe, [127, 139, 153])
blood_pressure['high'] = fuzz.trimf(blood_pressure.universe, [153, 157, 172])
blood_pressure['very_high'] = fuzz.trapmf(blood_pressure.universe, [154, 171, 350, 350])

blood_sugar['false'] = fuzz.trapmf(blood_sugar.universe, [0, 0, 105, 120])
blood_sugar['true'] = fuzz.trapmf(blood_sugar.universe, [105, 120, 200, 200])

cholesterol['low'] = fuzz.trapmf(cholesterol.universe, [0, 0, 151, 197])
cholesterol['medium'] = fuzz.trimf(cholesterol.universe, [188, 215, 250])
cholesterol['high'] = fuzz.trimf(cholesterol.universe, [217, 263, 307])
cholesterol['very_high'] = fuzz.trapmf(cholesterol.universe, [281, 347, 600, 600])

maximum_heart_rate['low'] = fuzz.trapmf(maximum_heart_rate.universe, [0, 0, 100, 141])
maximum_heart_rate['medium'] = fuzz.trimf(maximum_heart_rate.universe, [111, 152, 194])
maximum_heart_rate['high'] = fuzz.trapmf(maximum_heart_rate.universe, [152, 210, 600, 600])

exercise['false'] = fuzz.gaussmf(exercise.universe, 0, 0.00001)
exercise['true'] = fuzz.gaussmf(exercise.universe, 1, 0.00001)

thallium['normal'] = fuzz.gaussmf(thallium.universe, 3, 0.00001)
thallium['medium'] = fuzz.gaussmf(thallium.universe, 6, 0.00001)
thallium['high'] = fuzz.gaussmf(thallium.universe, 7, 0.00001)

sex['male'] = fuzz.gaussmf(sex.universe, 0, 0.00001)
sex['female'] = fuzz.gaussmf(sex.universe, 1, 0.00001)

ecg['normal'] = fuzz.trapmf(ecg.universe, [-0.5, -0.5, 0, 0.4])
ecg['abnormal'] = fuzz.trimf(ecg.universe, [0.2, 1, 1.8])
ecg['hypertrophy'] = fuzz.trapmf(ecg.universe, [1.4, 1.9, 2.5, 2.5])

old_peak['low'] = fuzz.trapmf(old_peak.universe, [0, 0, 1, 2])
old_peak['risk'] = fuzz.trimf(old_peak.universe, [1.5, 2.8, 4.2])
old_peak['terrible'] = fuzz.trapmf(old_peak.universe, [2.5, 4, 10, 10])

health['healthy'] = fuzz.trapmf(health.universe, [0, 0, 0.25, 1])
health['sick_1'] = fuzz.trimf(health.universe, [0, 1, 2])
health['sick_2'] = fuzz.trimf(health.universe, [1, 2, 3])
health['sick_3'] = fuzz.trimf(health.universe, [2, 3, 4])
health['sick_4'] = fuzz.trapmf(health.universe, [3, 3.75, 4, 4])

rules = [
    # RULE 1: IF (age IS very_old) AND (chest_pain IS atypical_anginal) THEN health IS sick_4;
    ctrl.Rule(age['very_old'] & chest_pain['atypical_anginal'], health['sick_4']),

    # RULE 2: IF (maximum_heart_rate IS high) AND (age IS old) THEN health IS sick_4;
    ctrl.Rule(maximum_heart_rate['high'] & age['old'], health['sick_4']),

    # RULE 3: IF (sex IS male) AND (maximum_heart_rate IS medium) THEN health IS sick_3;
    ctrl.Rule(sex['male'] & maximum_heart_rate['medium'], health['sick_3']),

    # RULE 4: IF (sex IS female) AND (maximum_heart_rate IS medium) THEN health IS sick_2;
    ctrl.Rule(sex['female'] & maximum_heart_rate['medium'], health['sick_2']),

    # RULE 5: IF (chest_pain IS non_aginal_pain) AND (blood_pressure IS high) THEN health IS sick_3;
    ctrl.Rule(chest_pain['non_aginal_pain'] & blood_pressure['high'], health['sick_3']),

    # RULE 6: IF (chest_pain IS typical_anginal) AND (maximum_heart_rate IS medium) THEN health IS sick_2;
    ctrl.Rule(chest_pain['typical_anginal'] & maximum_heart_rate['medium'], health['sick_2']),

    # RULE 7: IF (blood_sugar IS true) AND (age IS mild) THEN health IS sick_3;
    ctrl.Rule(blood_sugar['true'] & age['mild'], health['sick_3']),

    # RULE 8: IF (blood_sugar IS false) AND (blood_pressure IS very_high) THEN health IS sick_2;
    ctrl.Rule(blood_sugar['false'] & blood_pressure['very_high'], health['sick_2']),

    # RULE 9: IF (chest_pain IS asymptomatic) OR (age IS very_old) THEN health IS sick_1;
    ctrl.Rule(chest_pain['asymptomatic'] | age['very_old'], health['sick_1']),

    # RULE 10: IF (blood_pressure IS high) OR (maximum_heart_rate IS low) THEN health IS sick_1;
    ctrl.Rule(blood_pressure['high'] | maximum_heart_rate['low'], health['sick_1']),

    # RULE 11: IF (chest_pain IS typical_anginal) THEN health IS healthy;
    ctrl.Rule(chest_pain['typical_anginal'], health['healthy']),

    # RULE 12: IF (chest_pain IS atypical_anginal) THEN health IS sick_1;
    ctrl.Rule(chest_pain['atypical_anginal'], health['sick_1']),

    # RULE 13: IF (chest_pain IS non_aginal_pain) THEN health IS sick_2;
    ctrl.Rule(chest_pain['non_aginal_pain'], health['sick_2']),

    # RULE 14: IF (chest_pain IS asymptomatic) THEN health IS sick_3;
    ctrl.Rule(chest_pain['asymptomatic'], health['sick_3']),

    # RULE 15: IF (chest_pain IS asymptomatic) THEN health IS sick_4;
    ctrl.Rule(chest_pain['asymptomatic'], health['sick_4']),

    # RULE 16: IF (sex IS female) THEN health IS sick_1;
    ctrl.Rule(sex['female'], health['sick_1']),

    # RULE 17: IF (sex IS male) THEN health IS sick_2;
    ctrl.Rule(sex['male'], health['sick_2']),

    # RULE 18: IF (blood_pressure IS low) THEN health IS healthy;
    ctrl.Rule(blood_pressure['low'], health['healthy']),

    # RULE 19: IF (blood_pressure IS medium) THEN health IS sick_1;
    ctrl.Rule(blood_pressure['medium'], health['sick_1']),

    # RULE 20: IF (blood_pressure IS high) THEN health IS sick_2;
    ctrl.Rule(blood_pressure['high'], health['sick_2']),

    # RULE 21: IF (blood_pressure IS high) THEN health IS sick_3;
    ctrl.Rule(blood_pressure['high'], health['sick_3']),

    # RULE 22: IF (blood_pressure IS very_high) THEN health IS sick_4;
    ctrl.Rule(blood_pressure['very_high'], health['sick_4']),

    # RULE 23: IF (cholesterol IS low) THEN health IS healthy;
    ctrl.Rule(cholesterol['low'], health['healthy']),

    # RULE 24: IF (cholesterol IS medium) THEN health IS sick_1;
    ctrl.Rule(cholesterol['medium'], health['sick_1']),

    # RULE 25: IF (cholesterol IS high) THEN health IS sick_2;
    ctrl.Rule(cholesterol['high'], health['sick_2']),

    # RULE 26: IF (cholesterol IS high) THEN health IS sick_3;
    ctrl.Rule(cholesterol['high'], health['sick_3']),

    # RULE 27: IF (cholesterol IS very_high) THEN health IS sick_4;
    ctrl.Rule(cholesterol['very_high'], health['sick_4']),

    # RULE 28: IF (blood_sugar IS true) THEN health IS sick_2;
    ctrl.Rule(blood_sugar['true'], health['sick_2']),

    # RULE 29: IF (ECG IS normal) THEN health IS healthy;
    ctrl.Rule(ecg['normal'], health['healthy']),

    # RULE 30: IF (ECG IS normal) THEN health IS sick_1;
    ctrl.Rule(ecg['normal'], health['sick_1']),

    # RULE 31: IF (ECG IS abnormal) THEN health IS sick_2;
    ctrl.Rule(ecg['abnormal'], health['sick_2']),

    # RULE 32: IF (ECG IS hypertrophy) THEN health IS sick_3;
    ctrl.Rule(ecg['hypertrophy'], health['sick_3']),

    # RULE 33: IF (ECG IS hypertrophy) THEN health IS sick_4;
    ctrl.Rule(ecg['hypertrophy'], health['sick_4']),

    # RULE 34: IF (maximum_heart_rate IS low) THEN health IS healthy;
    ctrl.Rule(maximum_heart_rate['low'], health['healthy']),

    # RULE 35: IF (maximum_heart_rate IS medium) THEN health IS sick_1;
    ctrl.Rule(maximum_heart_rate['medium'], health['sick_1']),

    # RULE 36: IF (maximum_heart_rate IS medium) THEN health IS sick_2;
    ctrl.Rule(maximum_heart_rate['medium'], health['sick_2']),

    # RULE 37: IF(maximum_heart_rate IS high) THEN health IS sick_3;
    ctrl.Rule(maximum_heart_rate['high'], health['sick_3']),

    # RULE 38: IF(maximum_heart_rate IS high) THEN health IS sick_4;
    ctrl.Rule(maximum_heart_rate['high'], health['sick_4']),

    # RULE 39: IF (exercise IS true) THEN health IS sick_2;
    ctrl.Rule(exercise['true'], health['sick_2']),

    # RULE 40: IF (old_peak IS low) THEN health IS healthy;
    ctrl.Rule(old_peak['low'], health['healthy']),

    # RULE 41: IF (old_peak IS low) THEN health IS sick_1;
    ctrl.Rule(old_peak['low'], health['sick_1']),

    # RULE 42: IF (old_peak IS terrible) THEN health IS sick_2;
    ctrl.Rule(old_peak['terrible'], health['sick_2']),

    # RULE 43: IF (old_peak IS terrible) THEN health IS sick_3;
    ctrl.Rule(old_peak['terrible'], health['sick_3']),

    # RULE 44: IF (old_peak IS risk) THEN health IS sick_4;
    ctrl.Rule(old_peak['risk'], health['sick_4']),

    # RULE 45: IF (thallium IS normal) THEN health IS healthy;
    ctrl.Rule(thallium['normal'], health['healthy']),

    # RULE 46: IF (thallium IS normal) THEN health IS sick_1;
    ctrl.Rule(thallium['normal'], health['sick_1']),

    # RULE 47: IF (thallium IS medium) THEN health IS sick_2;
    ctrl.Rule(thallium['medium'], health['sick_2']),

    # RULE 48: IF (thallium IS high) THEN health IS sick_3;
    ctrl.Rule(thallium['high'], health['sick_3']),

    # RULE 49: IF (thallium IS high) THEN health IS sick_4;
    ctrl.Rule(thallium['high'], health['sick_4']),

    # RULE 50: IF (age IS young) THEN health IS healthy;
    ctrl.Rule(age['young'], health['healthy']),

    # RULE 51: IF (age IS mild) THEN health IS sick_1;
    ctrl.Rule(age['mild'], health['sick_1']),

    # RULE 52: IF (age IS old) THEN health IS sick_2;
    ctrl.Rule(age['old'], health['sick_2']),

    # RULE 53: IF (age IS old) THEN health IS sick_3;
    ctrl.Rule(age['old'], health['sick_3']),

    # RULE 54: IF (age IS very_old) THEN health IS sick_4;
    ctrl.Rule(age['very_old'], health['sick_4'])
]

diagnosis_ctrl = ctrl.ControlSystem(rules)
diagnosis = ctrl.ControlSystemSimulation(diagnosis_ctrl)
