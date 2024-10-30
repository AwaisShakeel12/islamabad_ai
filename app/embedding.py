
import os
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from .splitter import text_chunks

GOOGLE_APPLICATION_CREDENTIALS = r""

from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file(GOOGLE_APPLICATION_CREDENTIALS)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

genai.configure(api_key='')





embedding = GoogleGenerativeAIEmbeddings(model='models/embedding-001')
vectorStore = FAISS.from_documents(text_chunks, embedding=embedding)
retiver = vectorStore.as_retriever()