from sqlmodel import Session, select

from DBModels.db_creation import engine
from dataStr.candidate_profile import CandidateProfile

with Session(engine) as session:
    candidates = session.exec(select(CandidateProfile)).all()

    for candidate in candidates:
        print(candidate)