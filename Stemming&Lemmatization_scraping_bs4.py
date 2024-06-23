from bs4 import BeautifulSoup                         # For parsing HTML content
import requests                                       #  For making HTTP requests to fetch web content
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet                       # For accessing the WordNet lexical database
from nltk import pos_tag
import nltk

# Downloading the necessary nltk data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Function to convert nltk POS tag to wordnet POS tag
def wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

# Apply stemming and lemmatization
def stem_and_lemmatize(text):
    words = word_tokenize(text)                                               # Tokenize the text into words
    pos_tags = pos_tag(words)                                                 # Get the POS tags for each word
    stemmed_words = [stemmer.stem(word) for word in words]
    lemmatized_words = []
    for word, tag in pos_tags:
        WT = wordnet_pos(tag)
        if WT is None:
            lemmatized_words.append(lemmatizer.lemmatize(word))
        else:
            lemmatized_words.append(lemmatizer.lemmatize(word,pos = WT))
    pos_tags_only = [tag for _, tag in pos_tags] 
    return words, stemmed_words, lemmatized_words, pos_tags_only
url = "https://en.wikipedia.org/wiki/Oswald_(TV_series)" 

# To Fetch the HTML content
response = requests.get(url)
html_content = response.content

# To parse html using beautifulsoup
soup = BeautifulSoup(html_content,'html.parser')

# Extract article text (assuming article is in <p> tags)
article_text = ''.join([p.get_text()for p in soup.find_all('p')])             #  Extracts the text from all <p> tags and joins them into a single string.

# Preprocess the article text
words,stemmed_words, lemmatized_words, pos_tags = stem_and_lemmatize(article_text)

# To print results in tabular form
print(f"{'Word':<15} {'POS':<10} {'Stem':<15} {'Lemma':<15}")                 # To print the header of the table
print("="*55)                                                                 # To print a line to separate the header from the content
for word, pos, stem, lemma in zip(words, pos_tags, stemmed_words, lemmatized_words):
    print(f"{word:<15} {pos:<10} {stem:<15} {lemma:<15}")