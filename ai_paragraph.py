import os
import requests
from bs4 import BeautifulSoup
import spacy

def load_spacy_model():
  try:
    return spacy.load('en_core_web_sm')
  except:
    print("""Have you downloaded the model yet? Try runng this in your terminal: 
    > python -m spacy download en_core_web_sm""")
    exit(1)

nlp = load_spacy_model()

ACCEPTED_POS = ('PROPN', 'NOUN', 'VERB')
AMT_WORDS_FOR_AI = 24

def fetch_description(project_link):
  """Return a hackathon project's description"""
  response = requests.get(project_link)
  if response.status_code != 200:
    return ""

  html = response.text
  soup = BeautifulSoup(html, "html.parser")
  return soup.find('div',{'id':"app-details-left"})

def pos_frequency(project_gallery_cards):
  """Point of speech frequency returns a dictionary of the most frequent words in project descriptions scraped from Devpost hackathons."""
  print(f"Calculating most frequent words for {len(project_gallery_cards)} projects")
  frequencies = {}

  for project_gallery_card in project_gallery_cards:
    project_link = project_gallery_card.get("href")
    if project_link == None:
      continue

    description = fetch_description(project_link)
    
    doc = nlp(description.text)

    for token in doc:
      if token.pos_ in ACCEPTED_POS:
        if token.lemma_ in frequencies:
          frequencies[token.lemma_] +=1
        elif token.lemma_ not in frequencies:
          frequencies[token.lemma_] = 1

  return frequencies

def fetch_top_words_from_devpost():
  """Returns a list of most frequent words in devpost hackathon projects"""
  print(f"Fetching top words from devpost")
  response = requests.get("https://devpost.com/software")
  html = response.text

  soup = BeautifulSoup(html, "html.parser")
  project_gallery_cards = soup.findAll('a',{'class':"block-wrapper-link fade link-to-software"})

  ascending_word_freq_dict = pos_frequency(project_gallery_cards)
  word_freq_dict = {
    k: v for k, v in sorted(ascending_word_freq_dict.items(), 
    key=lambda item: item[1],reverse = True)
  }

  words = []
  for word in word_freq_dict:
    words.append(word)
  
  return words

def generate_ai_paragraph(words):
  """Returns a generated paragraph inspired by the words provided"""
  print("Generating AI Paragraph")
  ai_data = ' '.join(words[0:AMT_WORDS_FOR_AI])
  r = requests.post(
      "https://api.deepai.org/api/text-generator",
      data={
          'text': ai_data,
      },
      headers={'api-key': os.environ['API_KEY']}
  )
  return r.json()["output"]

def generate(): 
  top_words = fetch_top_words_from_devpost()
  paragraph = generate_ai_paragraph(top_words)
  # Omit first 25 words - typically are bad
  clean_paragraph = ' '.join(paragraph.split(' ')[25:])
  print(clean_paragraph)
  return clean_paragraph

if __name__ == "__main__":
    generate()

os.environ['API_KEY']
