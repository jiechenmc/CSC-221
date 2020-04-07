# Web scraping
# 4/7/20
# CSC221 M4HW – Web Scraping
# Jie Chen

# No user Input
# Write the html of python.org into python.txt
# Program will display the number of words senteces and nounphrases

from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from textblob import TextBlob
import requests

# Getting Soup
url = requests.get("https://www.python.org")
soup = BeautifulSoup(url.content, "html5lib")
text = soup.get_text(strip=True)

# Writing the html to a textfile
with open("python.txt", "w", encoding="utf-8") as f:
    f.write(soup.prettify())


# Tokenizing the text
blob = TextBlob(text)
stop_words = stopwords.words("english")
words = [word for word in blob.words if word not in stop_words]
sentences = blob.sentences
noun_phrases = blob.noun_phrases

# Printing the number of words, sentences, and nounphrases
print(f"There is {len(words)} words")
print(f"There is {len(sentences)} sentences")
print(f"There is {len(noun_phrases)} nounphrases")
