from bs4 import BeautifulSoup
import urllib.request as req
from nltk.tokenize import word_tokenize

url1 = "https://www.opentable.com/r/the-woo-new-york?avt=eyJ2IjoxLCJtIjowLCJwIjowfQ&corrid=2dd34235-2e9c-4681-bd3b-5b2a90943fc6&p=2&sd=2020-05-07+19%3A00"
html1 = req.urlopen(url1)
doc1 = BeautifulSoup(html1,"html.parser")
review0 = doc1.find_all(class_="reviewBodyContainer oc-reviews-8107696f")[0].text

text = "It's an amazing experience here. I love you"

# tokenize
from nltk.tokenize import word_tokenize
tokenized_text = word_tokenize(review0)
print(tokenized_text)

# 불용어 제거
from nltk.corpus import stopwords
# stopwords.words("english") -> 영어 불용어 list를 리턴한다.
nltk_stopwords = stopwords.words("english")
nltk_stopwords.extend([",",".","!", "’", "\"", "\'"])

# stopwords가 소문자 list를 반환하여 소문자로 변환해야 한다.
word_token = [word for word in tokenized_text if not word.lower() in nltk_stopwords]
print(word_token)

# Stemming

from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
ps = PorterStemmer()
ls = LancasterStemmer()
lem = WordNetLemmatizer()

def normalize_word(word):
    init_word = word
    res_word = ps.stem(word)
    if init_word == res_word:
        res_word = ls.stem(res_word)
    pos_list = ["v", "a", "n", "r"]
    for lem_pos in pos_list:
        init_lem_word = res_word
        res_word = lem.lemmatize(res_word, pos=lem_pos)
        if init_lem_word != res_word: break
    return res_word

# result = [normalize_word(word) for word in word_token]
print(normalize_word('sure'))
    
# from nltk.probability import FreqDist

# # sudo python -m nltk.downloader -d /usr/local/share/nltk_data averaged_perceptron_tagger
# from nltk.corpus import brown

reviews_token_array = []
for p in range(len(Delta_reviews["reviews"])):
    reviews_token_array.append(word_tokenize(Delta_reviews["reviews"][p]))

reviews_token_array