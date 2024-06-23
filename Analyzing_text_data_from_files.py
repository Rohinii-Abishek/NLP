
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import nltk

# Downloading the necessary nltk data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Initialize the stemmer and Lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
# Analyzing text data from files
with open("saved_paragraph.txt",'r')as file:
    text = file.read()

# Tokenize the text
words = word_tokenize(text) 

# Applying stemming and lemmatization
print("Original text:", text[:200])
for word in words:
    stemmed_words = [stemmer.stem(word)]
    print("stemmed words :",'' .join(stemmed_words[:200]))
for word in words:
    lemmatized_words = [lemmatizer.lemmatize(word)]  
    print("lemmatized words :"''.join(lemmatized_words[:200])) 