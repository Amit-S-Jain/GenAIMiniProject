from sqlmodel import SQLModel, create_engine
from typing import Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.types import JSON
from datetime import datetime
from AIEngine.dataStr.candidate_profile import CandidateProfile
# models.candidate_profile import CandidateProfile
from AIEngine.dataStr.job_profile import JobProfile
from AIEngine.dataStr.job_match import JobMatch

DATABASE_URL = "sqlite:///../db.sqlite3"

engine = create_engine(
    DATABASE_URL,
    echo=True
)


def create_database():
    SQLModel.metadata.create_all(engine)

# ****************Candidate_profile.py**********************

# *********************job_profile.py**************************

# *********************job_match.py*****************************

# *********************create_db.py*****************************

if __name__ == "__main__":
    create_database()
    print("Database created successfully.")

