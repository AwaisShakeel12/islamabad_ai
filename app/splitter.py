
from langchain_text_splitters import RecursiveCharacterTextSplitter
from .data_loader import combine

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
text_chunks = text_splitter.split_documents(combine)