from PyPDF2 import PdfReader
import requests
import io
from bs4 import BeautifulSoup

url=requests.get("https://wgms.ch/downloads/Cogley_etal_2011.pdf")

page_start = 29
page_end = 110
with io.BytesIO(url.content) as f:
    pdf = PdfReader(f)
    text = []
    for i in range(page_start, page_end):
        page = pdf.pages[i]
        text.append(page.extract_text())
    text = '\n'.join(text)

# Write to file
with open("data/glossary_of_glacier_mass_balance.txt", "wt") as f:
    f.write(text)

