

from langchain.document_loaders import UnstructuredURLLoader
from .data_scrap import documents

urls = [

    'https://en.wikipedia.org/wiki/Islamabad_United',
    'https://www.espncricinfo.com/team/islamabad-united-953843',
    'https://en.wikipedia.org/wiki/2021_Islamabad_United_season',
    'https://en.wikipedia.org/wiki/2022_Islamabad_United_season',
    'https://en.wikipedia.org/wiki/2023_Islamabad_United_season',
    'https://en.wikipedia.org/wiki/2024_Islamabad_United_season'
   
]


loader = UnstructuredURLLoader(urls=urls)
data= loader.load()


combine = data + documents