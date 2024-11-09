import sqlalchemy as db
from sqlalchemy import func
from dbmodels import Base, StatuseBase, AutorizBase, DepartmentBase, CoachBase, TariffBase, TeamBase, SportsmenBase, TimetableBase, TrialLesonBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine, AsyncSession

database_url = 'mysql+aiomysql://root:password@localhost/sportsclub'
engine = db.create_as

Session = sessionmaker(engine)

with Session() as session:
    pass

def create_db_and_tables():
    Base.metadata.create_all(engine)

create_db_and_tables()