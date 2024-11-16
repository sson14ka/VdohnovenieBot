# app/api/router.py

from fastapi import APIRouter, HTTPException
from app.database.dbconnect import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/status")
async def get_status():
    return {"status": "Bot is up and running!"}

@router.get("/users/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
