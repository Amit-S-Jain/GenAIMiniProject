from AIEngine.DBModels.db_creation import create_database
from AIEngine.DBModels.insert_data import DBInsert
from AIEngine.resume_parser.localLLMforResume import resume_llm_call
# from AIEngine.DBModels.deleteCandidate import DeleteCandidate

class MainClass:
    def parse_resume(file_path):
        # resume = input("Provide your resume path : ")
        # file_path = "C:/Users/amits/Desktop/GenAi/NaukriAgent/DjangoProject/AIEngine/resume/"+resume+".pdf"
        print(file_path)


        llm_response = resume_llm_call.resume_llmCall(file_path)
        print("********************LLM Response********************************")
        print(llm_response)
        # create_database()
        obj = DBInsert()

        print("\n\n********************Extract JSON********************************")
        data = obj.extract_json(llm_response)
        print(data)

        print("\n\n********************Normalize Candidate********************************")
        data = obj.normalize_candidate(data)

        print("The Resume Data is as Below:")
        print(data)

        return data

        # print("\n\n********************Data Insertion********************************")
        # data = obj.DBinsertOriginal(data)
        # print(data)

    # print("\n\n********************LLM Response********************************")
    # print(data)

    # # delete = DeleteCandidate.Del("Amitsjain9161@gmail.com")

if __name__ == "__main__":
    obj = MainClass()
    resume = input("Provide your resume path : ")
    file_path = "C:/Users/amits/Desktop/GenAi/NaukriAgent/DjangoProject/AIEngine/resume/"+resume+".pdf"
    obj.parse_resume(file_path)