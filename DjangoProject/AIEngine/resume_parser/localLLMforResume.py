from ollama import chat
# from resume_reader import resume_text
from .resume_parser_doclink import resume_reader_txt
from datetime import datetime
from dataStr.candidate_profile import CandidateProfile
from DBModels.db_schema import DBSchema
from resume_parser.resume_parser_doclink import resume_reader_txt

class resume_llm_call:
    def resume_llmCall(file_path):
        resume_txt = resume_reader_txt(file_path)
        print("\n*********Resume Text*******\n",resume_txt)

        current_date = datetime.now()
        # candidate_profile = CandidateProfile().model_json_schema()
        candidate_profile = DBSchema.print_schema("candidates_candidates")

        # print("\n\n**************************CANDIDATE PROFILE SCHEMA**********************\n\n")
        # print(candidate_profile)
        

        prompt = f'''Return only valid JSON matching the database schema.

            Rules:

            Do not return arrays ([]) or nested objects ({{}}).
            Every field must be a string, number, boolean, or null.
            Convert lists into comma-separated strings.
            preferred_roles, preferred_locations, skills, languages_know, certifications, and education must be stored as comma-separated strings.
            education format: Degree - Institution (CGPA: X.XX).
            Convert experience values such as "4+ years" into numeric values (4.0).
            Use JSON null, not the string "null".
            Return only the JSON object with no markdown or explanatory text.
            **Structure :** {candidate_profile}
            **Today's date is :** {current_date}
            **Resume Data :** {resume_txt}
            '''
        # prompt = input("\n\n********************************************************************** \nEnter Prompt : ")
        response = chat(
            model="llama3.1:8b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        # print(response["message"]["content"])
        return response["message"]["content"]

if __name__ == "__main__":
    file_path = "C:/Users/amits/Desktop/GenAi/NaukriAI/parser/resume2.pdf"
    resume_llm_call.resume_llmCall(file_path)