

from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from .embedding import retiver

from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnablePassthrough

from .prompts1 import prompt_template



llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Updated chain creation using the new method
chain = (
    {
        "context": lambda question: [doc.page_content for doc in retiver.invoke(question)],
        "question": RunnablePassthrough()
    }
    | prompt_template
    | llm
    | StrOutputParser()
)
