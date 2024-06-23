# NLTK for stemming and lemmatization with POS tagging to improve the lemmatization results
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet
import nltk

# Downloading the necessary nltk data
nltk.download('punkt')
nltk.download('averaged_Perceptron_tagger')
nltk.download('wordnet')

# Initialize the stemmer and Lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Function to convert nltk POS tag to wordnet POS tag
def wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith ('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

# The sentence
sentence = "The cook was boiling water and chopped vegetables before frying and baking them, making the preparation complete."

# Tokenize the sentence
words = word_tokenize(sentence)

# Apply POS tagging
pos_tags = pos_tag(words)

# Apply Stemming and Lemmatization
for word in words:
    stemmed_words = [stemmer.stem(word)]
    print("Stemmed words :", stemmed_words)
lemmatized_words = []
for word, tag in pos_tags:
    WT = wordnet_pos(tag)
    if WT is None:
        lemmatized_words.append(lemmatizer.lemmatize(word))
    else:
        lemmatized_words.append(lemmatizer.lemmatize(word,pos = WT))
print("Lemmatized words :",lemmatized_words)        