

import os
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'


from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQAWithSourcesChain
# from langchain.embeddings import HuggingFaceEmbeddings



from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough


from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai


from selenium import webdriver
from bs4 import BeautifulSoup
# Convert table data to documents
from langchain.docstore.document import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


GOOGLE_APPLICATION_CREDENTIALS = r""

from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file(GOOGLE_APPLICATION_CREDENTIALS)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

genai.configure(api_key='')






driver = webdriver.Chrome()

# urls = [
#     'https://en.wikipedia.org/wiki/Islamabad_United',
#     'https://www.espncricinfo.com/team/islamabad-united-953843',
#     'https://en.wikipedia.org/wiki/2024_Islamabad_United_season'
# ]

wiki =  'https://en.wikipedia.org/wiki/Islamabad_United'
islu2021 ='https://en.wikipedia.org/wiki/2021_Islamabad_United_season',
islu2022 =  'https://en.wikipedia.org/wiki/2022_Islamabad_United_season',
islu2023 =  'https://en.wikipedia.org/wiki/2023_Islamabad_United_season',
islu_2024 ='https://en.wikipedia.org/wiki/2024_Islamabad_United_season'
urls = f'{wiki}{islu_2024}'

# Load the webpage
driver.get(urls)

# Get the page source after JavaScript execution
html_content = driver.page_source

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all tables in the page
tables = soup.find_all('table')

# Extract table data
table_data = []
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all(['td', 'th'])
        row_data = [cell.get_text(strip=True) for cell in cells]
        table_data.append(row_data)

# Close the driver
driver.quit()




documents = []
for row in table_data:
    # Convert the row into a single string
    row_content = ' '.join(row)
    # Create a Document object with the row content
    documents.append(Document(page_content=row_content))

