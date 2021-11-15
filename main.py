import requests
from bs4 import BeautifulSoup
from collections import Counter
import spacy
import re
import urllib.request

nlp = spacy.load('en_core_web_sm')
pie = 'man, Jimmy Jimmy really likes pie!'
doc = nlp(pie)

results = []
ACCEPTED_POS = ('PROPN', 'NOUN', 'VERB')

def pos_frequency(str):
  doc = nlp(str)
  for token in doc:
    if token.pos_ in ACCEPTED_POS:
        results.append(token)


  frequencies = {}
  for token in results:
    if token.lemma_ in frequencies:
      frequencies[token.lemma_] +=1
    elif token.lemma_ not in frequencies:
      frequencies[token.lemma_] = 1
  return frequencies


url = "https://devpost.com/software"

#html = url("https://devpost.com/software")

response = requests.get(url)
html = response.text
link = re.findall("href",'block-wrapper-link fade link-to-software')

soup = BeautifulSoup(html, "html.parser")
projects = soup.findAll('a',{'class':"block-wrapper-link fade link-to-software"})
for project in projects:
 print(project.get('href'))
 all_dict = pos_frequency(project.text)
 print(all_dict)
for keys in all_dict:
  print(keys)




  
'''common_words = soup.text.split()
  print(project.get('href'))
  print(Counter(common_words).most_common(50))

import en_core_web_sm
nlp = en_core_web_sm.load()

soup.find_all("p", text=re.complie("UK"))'''

