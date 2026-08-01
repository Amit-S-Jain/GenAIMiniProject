from sqlmodel import SQLModel, create_engine
from typing import Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.types import JSON
from datetime import datetime


class JobProfile(SQLModel, table=True):
    __tablename__ = "job_profiles"

    id: Optional[int] = Field(default=None, primary_key=True)

    # Source Information
    source: str = Field(index=True)              # Naukri, LinkedIn, Indeed
    external_job_id: Optional[str] = None
    job_url: str

    # Company Information
    company_name: str = Field(index=True)
    company_url: Optional[str] = None

    # Job Information
    job_title: str = Field(index=True)
    location: str
    employment_type: Optional[str] = None        # Full-Time, Contract
    work_mode: Optional[str] = None              # Remote, Hybrid, Onsite

    # Experience & Salary
    min_experience: Optional[float] = None
    max_experience: Optional[float] = None

    min_salary: Optional[float] = None
    max_salary: Optional[float] = None
    salary_currency: Optional[str] = "INR"

    # Skills
    skills: list[str] = Field(
        default_factory=list,
        sa_column=Column(JSON)
    )

    # Job Description
    description: str

    # Metadata
    posted_date: Optional[datetime] = None
    scraped_date: datetime = Field(default_factory=datetime.utcnow)

    is_active: bool = True
