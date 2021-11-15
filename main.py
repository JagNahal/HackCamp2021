import requests
from bs4 import BeautifulSoup
import spacy
import re

nlp = spacy.load('en_core_web_sm')

#'man, Jimmy Jimmy really likes pie!'


results = []
ACCEPTED_POS = ('PROPN', 'NOUN', 'VERB')

def pos_frequency(projects):
  frequencies = {}
  count = 0
  for project in projects:
    if project.get("href") == None:
      continue

    response = requests.get(project.get('href'))
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find('div',{'id':"app-details-left"})
    
    doc = nlp(div.text)
    count += 1

    for token in doc:
      if token.pos_ in ACCEPTED_POS:
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

results = pos_frequency(projects)
results ={k: v for k, v in sorted(results.items(), key=lambda item: item[1],reverse = True)}

keys = []
for key in results:
  keys.append(key)

keys = keys
ai_data = ' '.join(keys[0:24])
r = requests.post(
    "https://api.deepai.org/api/text-generator",
    data={
        'text': ai_data,
    },
    headers={'api-key': '41f74417-b15d-4dbb-b2c3-67511c6c3a2b'}
)
ai_paragraph = r.json()["output"]
print(ai_paragraph)


