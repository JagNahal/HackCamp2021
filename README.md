# AI Hackathon Description Generator

This fun hackathon project scrapes DevPost for a list of projects and individually grabs keywords based on frequency from project descriptions. 

The frequently used words are inputted to the Text Generation API from Deep Api to output a few paragraphs in an attempt to mimic hackathon project descriptions.

## Motivation

This was my first hackathon and forray into programming 🤓

## Setup 
1. Clone the project
2. Grab the model: `python -m spacy download en_core_web_sm` 
3. Run python main.py

## What we learned
- We learned about scraping, which is the process of grabbing data from HTML pages.
- How we can transform the scraped data into a format that can be accepted by the Text Generator API. We judiciously used 3rd party libraries in order to accomplish this. 

## Accomplishments that we're proud of
This project was a lot of fun! We were very happy to have _completed_ this hackathon project, despite our lack of experience. We were able to complete the goal as intended by looking into various technologies, and implementing them for our use case.

## What's next for hackathon description generator:

In the future, we want to do a better job of parsing out the key words from the project descriptions. At the moment, we're just selecting the most frequently used words in order to generate our project description. Furthermore, it would be useful to allow manual keywords to be added into our request to the Text Generator API to customize the output. #staytuned