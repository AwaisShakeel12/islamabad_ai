
from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_template("""
Your are a Professional Assistant. Your job is to answer the user's query  in a professional manner. 
If you don't know the context, say "I don't know."

Context: {context}
Question: {question}

Answer: """

)
