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
        """
        Extract JSON object from LLM response.
        """

        # Remove markdown code blocks if present
        match = re.search(r"```(?:json)?\s*(\{.*\})\s*```", llm_response, re.DOTALL)

        if match:
            json_string = match.group(1)
        else:
            # Fallback: find first { and last }
            start = llm_response.find("{")
            end = llm_response.rfind("}")

            if start == -1 or end == -1:
                raise ValueError("No JSON object found.")

            json_string = llm_response[start:end + 1]

        return json.loads(json_string)

    def normalize_candidate(self, data):

        list_fields = [
            "preferred_roles",
            "preferred_locations",
            "skills",
            "languages_know",
            "certifications",
            "education",
            "current_company"
        ]

        for field in list_fields:

            value = data.get(field)

            if isinstance(value, list):

                converted = []

                for item in value:

                    if isinstance(item, dict):
                        converted.append(
                            ", ".join(str(v) for v in item.values() if v)
                        )
                    else:
                        converted.append(str(item))

                data[field] = ", ".join(converted)

        # Convert experience values

        for field in ["total_experience", "relevant_experience"]:

            value = data.get(field)

            if isinstance(value, str):

                match = re.search(r"\d+(\.\d+)?", value)

                if match:
                    data[field] = float(match.group())
                else:
                    data[field] = None

        # Convert "null" string into None

        for key, value in data.items():

            if isinstance(value, str):

                if value.strip().lower() == "null":
                    data[key] = None

        return data