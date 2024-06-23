from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import spacy
import nltk
nltk.download('punkt')                                      #  Punkt tokenizer is a pre-trained model for tokenizing text into sentences and words
# Initialize stemmer & Spacy model
stemmer = PorterStemmer()
nlp = spacy.load('en_core_web_sm')

# The sentence
sentence = "The cook was boiling water and chopped vegetables before frying and baking them, making the preparation complete."

# Tokenize the sentence
words = word_tokenize(sentence)

# apply stemming and lemmatization
for word in words:
    stemmed_words = [stemmer.stem(word)]
    print("stemmed words :",''.join(stemmed_words))         # (.join)  prints the stemmed words as a single string.
for word in words:
    doc = nlp(word)
    lemma = doc[0].lemma_
    print("Lemmatized words :",''.join(lemma))