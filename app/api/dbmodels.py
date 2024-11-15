import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import String
from sqlalchemy import ForeignKey
from typing import Optional
from sqlalchemy import DECIMAL, DATE, TIME, BOOLEAN, BigInteger
from app.database.dbconnect import Base

class StatuseBase(Base):
    __tablename__ = "statuse"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    statuse_name: Mapped[str] = mapped_column(String(20))

    autoriz = relationship("autoriz", back_populates="statuse")


class AutorizBase(Base):
    __tablename__ = "autoriz"
    tg_user_id: Mapped[str] = mapped_column(String(40), unique=True, primary_key=True)
    statuse_id: Mapped[int]= mapped_column(ForeignKey("statuse.id"))

    statuse = relationship("statuse", back_populates="autoriz")
    coach = relationship("coach", back_populates="autoriz")
    sportsmen = relationship("sportsmen", back_populates="autoriz")


class DepartmentBase(Base):
    __tablename__ = "department"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), unique=True)
    city: Mapped[str] = mapped_column(String(20))
    street: Mapped[str] = mapped_column(String(20))
    house_number: Mapped[int] = mapped_column()
    building: Mapped[Optional[int]] = mapped_column()
    gym_rent: Mapped[float] = mapped_column(DECIMAL(8, 0))
    trial_lesson_price:Mapped[float] = mapped_column(DECIMAL(5,0))

    coach = relationship("coach", back_populates="department")
    tariff = relationship("tariff", back_populates="department")
    team = relationship("team", back_populates="department")


class CoachBase(Base):
    __tablename__ = "coach"
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[str] = mapped_column(ForeignKey("autoriz.tg_user_id"))
    name: Mapped[str] = mapped_column(String(20))
    surname: Mapped[str] = mapped_column(String(35))
    patronymic: Mapped[Optional[str]] = mapped_column(String(35))
    phone: Mapped[str] = mapped_column(String(12), unique=True)
    hire_date: Mapped[datetime.date] = mapped_column(DATE)
    salary: Mapped[float] = mapped_column(DECIMAL(7,0))
    department_id: Mapped[int] = mapped_column(ForeignKey("department.id"))

    department = relationship("department", back_populates="coach")
    autoriz = relationship("autoriz", back_populates='coach')
    team = relationship("team", back_populates='coach')
    sportsmen = relationship("sportsmen", back_populates="coach")


class TariffBase(Base):
    __tablename__ = "tariff"
    id: Mapped[int] = mapped_column(primary_key=True)
    department_id: Mapped[int] = mapped_column(ForeignKey("department.id"))
    training_days: Mapped[str] = mapped_column(String(20))
    lengths_of_training: Mapped[str] = mapped_column(String(20))
    hours_per_week: Mapped[datetime.time] = mapped_column(TIME)
    price: Mapped[float] = mapped_column(DECIMAL(7,0))

    department = relationship("department", back_populates="tariff")
    team = relationship("team", back_populates="tariff")
    timetable = relationship("timetable", back_populates="tariff")


class TeamBase(Base):
    __tablename__ = "team"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(20))
    sportsmen_age: Mapped[str] = mapped_column(String(5))
    tariff_id: Mapped[int] = mapped_column(ForeignKey("tariff.id"))
    department_id: Mapped[int] = mapped_column(ForeignKey("department.id"))
    coach_id: Mapped[int] = mapped_column(ForeignKey("coach.id"))

    tariff = relationship("tariff", back_populates="team")
    department = relationship("department", back_populates="team")
    coach = relationship("coach", back_populates="team")


class SportsmenBase(Base):
    __tablename__ = "sportsmen"
    id:Mapped[int] = mapped_column(primary_key=True)
    tg_user_id: Mapped[str] = mapped_column(ForeignKey('autoriz.tg_user_id'))
    name: Mapped[str] = mapped_column(String(20))
    surname: Mapped[str] = mapped_column(String(35))
    patronymic: Mapped[Optional[str]] = mapped_column(String(35))
    phone: Mapped[str] = mapped_column(String(12), unique=True)
    birth_date: Mapped[datetime.date] = mapped_column(DATE)
    year_of_study: Mapped[int] = mapped_column()
    category: Mapped[Optional[str]] = mapped_column(String(35))
    payment_for_month: Mapped[bool] = mapped_column(BOOLEAN)
    coach_id: Mapped[int] = mapped_column(ForeignKey("coach.id"))
    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"))

    autoriz = relationship("autoriz", back_populates="sportsmen")
    coach = relationship("coach", back_populates="sportsmen")
    team = relationship('team', back_populates="sportsmen")


class TimetableBase(Base):
    __tablename__ = "timetable"
    id: Mapped[int] = mapped_column(primary_key=True)
    tariff_id: Mapped[int] = mapped_column(ForeignKey("tariff.id"))
    monday: Mapped[str] = mapped_column(String(20))
    tuesday: Mapped[str] = mapped_column(String(20))
    wednsday: Mapped[str] = mapped_column(String(20))
    thursday: Mapped[str] = mapped_column(String(20))
    friday: Mapped[str] = mapped_column(String(20))
    saturday: Mapped[str] = mapped_column(String(20))
    sunday: Mapped[str] = mapped_column(String(20))

    tariff = relationship("tariff", back_populates="timetable")


class TrialLesonBase(Base):
    __tablename__ = "trial_lessons"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    surname: Mapped[str] = mapped_column(String(35))
    patronymic: Mapped[Optional[str]] = mapped_column(String(35))
    birth_date: Mapped[datetime.date] = mapped_column(DATE)
    year_of_study: Mapped[int] = mapped_column()
    category: Mapped[Optional[str]] = mapped_column(String(35))
    department_id: Mapped[int]= mapped_column(ForeignKey("department.id"))

    department = relationship("department", back_populates="triallesson")
