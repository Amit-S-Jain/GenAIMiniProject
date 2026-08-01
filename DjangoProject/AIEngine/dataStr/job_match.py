from sqlmodel import SQLModel, create_engine
from typing import Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.types import JSON
from datetime import datetime

class JobMatch(SQLModel, table=True):
    __tablename__ = "job_matches"

    id: Optional[int] = Field(default=None, primary_key=True)

    # Foreign Keys
    candidate_id: int = Field(foreign_key="candidateprofile.id", index=True)
    job_id: int = Field(foreign_key="job_profiles.id", index=True)

    # AI Match Result
    match_score: float = Field(default=0.0)

    recommendation: str = Field(default="Not Evaluated")

    reasoning: str = ""

    # Skill Analysis
    matching_skills: list[str] = Field(
        default_factory=list,
        sa_column=Column(JSON)
    )

    missing_skills: list[str] = Field(
        default_factory=list,
        sa_column=Column(JSON)
    )

    additional_skills: list[str] = Field(
        default_factory=list,
        sa_column=Column(JSON)
    )

    # Status
    status: str = Field(default="Pending")

    applied: bool = Field(default=False)

    shortlisted: bool = Field(default=False)

    rejected: bool = Field(default=False)

    # Metadata
    matched_on: datetime = Field(default_factory=datetime.utcnow)

    last_updated: datetime = Field(default_factory=datetime.utcnow)
