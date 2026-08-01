from sqlmodel import Session, select

from DBModels.db_creation import engine
from dataStr.candidate_profile import CandidateProfile

class DeleteCandidate:
    def Del(email):
        with Session(engine) as session:
            statement = select(CandidateProfile).where(
                CandidateProfile.email == email
            )

            candidate = session.exec(statement).first()

            if candidate:
                session.delete(candidate)
                session.commit()
                print("Deleted successfully.")
            else:
                print("Candidate not found.")