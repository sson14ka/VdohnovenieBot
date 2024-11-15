from sqlalchemy import func
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine, AsyncSession
from dotenv import load_dotenv
import os
import logging

# Настройка логирования
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# Загрузка переменных окружения
load_dotenv()

# Конфигурация базы данных
database_url = os.getenv("DATABASE_URL", "mysql+aiomysql://root:password@localhost/sportsclub")
engine = create_async_engine(url=database_url)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession)

# Базовый класс для моделей
class Base(AsyncAttrs, DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

# Функция для корректного завершения работы
async def shutdown():
    await engine.dispose()

# Генератор сессий
async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
