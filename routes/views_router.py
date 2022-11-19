from fastapi import APIRouter
from controllers.views_controller import homepage
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/home", response_class=HTMLResponse)
def home():
    return homepage()
