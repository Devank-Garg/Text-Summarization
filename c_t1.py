import requests
from bs4 import BeautifulSoup
import re


def text(url):

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        
        paragraphs = soup.find_all(['p']) # extract all paragraphs, headings, lists, tables, and divs from the article
        text_data = []
        for element in paragraphs:
            text_data.append(element.get_text())

        
        text_string = ' '.join(text_data) # join the list of text strings into a single string
        if len(text_string)>1000:

          text_string=text_string[0:1000]
        else:
          text_string=text_string
        text_string=re.sub(r'[^\w\s]|\d|[\n]','',text_string)
        


        # print the text string
        return text_string