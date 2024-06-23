
from nltk.stem import PorterStemmer
import spacy 

# Initialize Stemmer & SpaCy model
stemmer = PorterStemmer()
nlp = spacy.load('en_core_web_sm')

# List of words
words = ["Cook", "Boiling", "Chopped", "Frying", "Baked", "Preparation"]

# Apply Stemming and Lemmatization
for word in words:
    stemmed_words = [stemmer.stem(word)]
    print("stemmed_words :",stemmed_words)

for word in words:
    doc = nlp(word)
    lemma = doc[0].lemma_
    print("Lemmatized_words : ",lemma)
