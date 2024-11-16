import sqlalchemy as db
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dbmodels import Base, StatuseBase, AutorizBase, DepartmentBase, CoachBase, TariffBase, TeamBase, SportsmenBase, TimetableBase, TrialLesonBase

# URL для подключения к базе данных MySQL
database_url = 'mysql+aiomysql://root:password@localhost/sportsclub'

# Создание асинхронного движка
engine = create_async_engine(database_url, echo=True)

# Создание асинхронного sessionmaker
AsyncSessionMaker = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Функция для создания базы данных и таблиц
async def create_db_and_tables():
    # Асинхронно создаем все таблицы, указанные в Base.metadata
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Пример использования сессии
async def run_session():
    async with AsyncSessionMaker() as session:
        # Пример запросов или работы с сессией
        pass

# Запуск создания таблиц
import asyncio
asyncio.run(create_db_and_tables())
