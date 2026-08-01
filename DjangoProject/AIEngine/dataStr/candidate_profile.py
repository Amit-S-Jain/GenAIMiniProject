from sqlmodel import SQLModel, create_engine
from typing import Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.types import JSON
from datetime import datetime


class CandidateProfile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str
    email: str
    phone: str
    total_experience: float

    current_company: Optional[str] = None
    current_role: Optional[str] = None
    current_ctc: Optional[float] = None
    expected_ctc: Optional[float] = None
    notice_period: Optional[str] = None

    preferred_locations: list = Field(
        default_factory=list,
        sa_column=Column(JSON)
    )

    preferred_roles: list = Field(
        default_factory=list,
        sa_column=Column(JSON)
    )

    skills: list = Field(
        default_factory=list,
        sa_column=Column(JSON)
    )

    certifications: list = Field(
        default_factory=list,
        sa_column=Column(JSON)
    )

    education: list = Field(
        default_factory=list,
        sa_column=Column(JSON)
    )

