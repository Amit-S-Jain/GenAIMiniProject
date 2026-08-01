from DBModels.db_creation import create_database
from DBModels.insert_data import DBInsert
from resume_parser.localLLMforResume import resume_llm_call
from DBModels.deleteCandidate import DeleteCandidate

file_path = "C:/Users/amits/Desktop/GenAi/NaukriAI/DjangoProject/resume/AmitJainResumeDotNet.pdf"
llm_response = resume_llm_call.resume_llmCall(file_path)
print("********************LLM Response********************************")
print(llm_response)
create_database()
obj = DBInsert()

print("\n\n********************Extract JSON********************************")
data = obj.extract_json(llm_response)
print(data)

# print("\n\n********************Normalize Candidate********************************")
# data = obj.normalize_candidate(data)
# print(data)

print("\n\n********************Data Insertion********************************")
data = obj.DBinsertOriginal(data)
print(data)

print("\n\n********************LLM Response********************************")
print(data)

# delete = DeleteCandidate.Del("Amitsjain9161@gmail.com")