# app/pages/router.py

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return HTMLResponse(content="Welcome to the bot platform!", status_code=200)

@router.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return HTMLResponse(content="About the bot platform", status_code=200)
