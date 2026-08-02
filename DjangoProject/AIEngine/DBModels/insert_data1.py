from sqlmodel import Session
from .db_creation import engine
from .db_creation import CandidateProfile
from resume_parser.localLLMforResume import resume_llm_call
import json
import re

# file_path = "C:/Users/amits/Desktop/GenAi/NaukriAI/resume/resume2.pdf"
# resume_response = resume_llm_call.resume_llmCall(file_path)
class DBInsert:
    def extract_json(self, llm_response: str) -> dict:

        blocks = re.findall(
            r"```(?:json)?\s*(.*?)\s*```",
            llm_response,
            re.DOTALL
        )

        for block in blocks:
            try:
                data = json.loads(block)

                if isinstance(data, dict) and "name" in data:
                    return data

            except json.JSONDecodeError:
                continue

        raise ValueError("Candidate JSON not found.")    

    def normalize_candidate(self, data: dict) -> CandidateProfile:

        data = data.copy()

        data.pop("id", "NULL")

        skills = []

        for x in data.get("skills", []):
            if isinstance(x, dict):
                print(x)  # Debug
                skills.append(x.get("item"))   # won't raise KeyError
            else:
                skills.append(x)

        data["skills"] = [s for s in skills if s]

        certifications = []
        for x in data.get("certifications", []):
            if isinstance(x, dict):
                print(x)  # Debug
                certifications.append(x.get("item"))   # won't raise KeyError
            else:
                certifications.append(x)

        data["certifications"] = [s for s in certifications if s]

        return CandidateProfile(**data)








    
    # # candidate = CandidateProfile(
    # #     name="Amit Jain",
    # #     email="amit@gmail.com",
    # #     phone="9876543210",
    # #     total_experience=6.5,
    # #     current_company="ABC",
    # #     skills=["Python", "FastAPI", "Azure"],
    # #     preferred_locations=["Pune", "Remote"]
    # # )

    def DBinsertOriginal(self, data):
        candidate = self.normalize_candidate(data)
        with Session(engine) as session:
            session.add(candidate)
            session.commit()