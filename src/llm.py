import os
from dotenv import  load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI 


load_dotenv()

# Loading Google API_KEY from .env file
GOOGLE_API_KEY= os.getenv('GOOGLE_API_KEY')
os.environ['GOOGLE_API_KEY']= GOOGLE_API_KEY


def ask_bot(message):
    llm= ChatGoogleGenerativeAI(model="gemini-pro")
    response= llm.invoke(message)
    return response.content


if __name__ == "__main__":
    print("Welcome to Gemini chatbot!!")
    message= ask_bot("What is the meaning of large language model?")
    print(message)