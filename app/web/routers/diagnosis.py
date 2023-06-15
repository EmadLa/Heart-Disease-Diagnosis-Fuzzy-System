from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.config.settings import settings
from app.domain.schema.symptom import SymptomsIn
from app.domain.usecase.symptom_uc import SymptomUC
from app.web.dependencies import get_symptom_uc

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.post("/diagnosis", response_class=HTMLResponse)
def diagno(
        request: Request,
        symptom_uc: SymptomUC = Depends(get_symptom_uc),
        sex: str = Form(...),
        age: str = Form(...),
        heart_rate: str = Form(...),
        blood_sugar: str = Form(...),
        blood_pressure: str = Form(...),
        cholesterol: str = Form(...),
        thallium: str = Form(...),
        ecg: str = Form(...),
        chest_pain: str = Form(...),
        exercise: str = Form(...),
        family_history: str = Form(...)
):
    chest_pain_dict = {
        "Typical Anginal": 1,
        "Atypical Anginal": 2,
        "Non Anginal pain": 3,
        "Asymptomatic": 4
    }
    symptom_in = SymptomsIn(
        sex=1 if sex == "male" else 0,
        age=int(age),
        maximum_heart_rate=int(heart_rate),
        blood_sugar=int(blood_sugar),
        blood_pressure=int(blood_pressure),
        cholesterol=int(cholesterol),
        thallium=int(thallium),
        ecg=int(ecg),
        chest_pain=chest_pain_dict[chest_pain],
        exercise=1 if exercise == "yes" else 0,
        old_peak=int(family_history) if family_history != "+10" else 10
    )
    result = symptom_uc.get_result(symptom_in)
    if result is not None:
        return templates.TemplateResponse(
            "result.html", {"request": request, "result": result.level, "base_url": settings.BASE_URL}
        )
