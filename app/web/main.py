from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.config.settings import settings
from .routers.diagnosis import router

templates = Jinja2Templates(directory="app/templates")

app = FastAPI()
app.include_router(router)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "base_url": settings.BASE_URL})
