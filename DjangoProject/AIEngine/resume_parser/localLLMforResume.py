from ollama import chat
# from resume_reader import resume_text
from .resume_parser_doclink import resume_reader_txt
from datetime import datetime
from dataStr.candidate_profile import CandidateProfile
from resume_parser.resume_parser_doclink import resume_reader_txt

class resume_llm_call:
    def resume_llmCall(file_path):
        resume_txt = resume_reader_txt(file_path)lo
        print("\n*********Resume Text*******\n",resume_txt)

        current_date = datetime.now()
        candidate_profile = CandidateProfile().model_json_schema()
        

        prompt = f'''Convert below Resume data into strictly provided model json schema way. Don't give anything extra that the structure. Also mention NULL in case of anything missing.
            Structure : {candidate_profile}
            Also today's date is : {current_date}
            Resume Data : {resume_txt}
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