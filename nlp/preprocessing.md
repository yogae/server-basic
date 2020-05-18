# preprocessing

## Tokenization

`punkt` package를 설치한다.

```bash
sudo python -m nltk.downloader -d /usr/local/share/nltk_data punkt
```

토큰의 기준을 단어로 하는 경우, 단어 토큰화라고 한다. ”It's an amazing experience here.”문장을 단어를 기준으로 tokenize하면 아래와 같다. 

```python
text = "It's an amazing experience here."
from nltk.tokenize import word_tokenize
tokenized = word_tokenize(text) #['It', "'s", 'an', 'amazing', 'experience', 'here', '.']
```

문장 단위로 토큰화하는 방법을 알아본다.

```python
from nltk.tokenize import sent_tokenize
text="I am actively looking for Ph.D. students. and you are a Ph.D student."
print(sent_tokenize(text)) # ['I am actively looking for Ph.D. students.', 'and you are a Ph.D student.']
```

NLTK는 단순히 온점을 구분자로 하여 문장을 구분하지 않았기 때문에, Ph.D.를 문장 내의 단어로 인식하여 성공적으로 인식하는 것을 볼 수 있다.

## 불용어(Stopword) 확인

단어 토큰 중 의미를 가지지 않는 단어 토큰을 제거한다. 예를들어 영어에서 a, an, the, i, you 등이 의미를 가지지 않는 불용어이다.

```python
from nltk.corpus import stopwords
nltk_stopwords = stopwords.words("english")
```

`stopwords.words("english")`는 영어의 불용어를 반환한다. 소문자 list를 반환하므로 소문자로 변환하여 string비교를 진행한다.

```python
word_token = [word for word in tokenized_text if not word.lower() in nltk_stopwords]
```

word_token은 불용어가 제거된 string list만 남게된다.

## 어간 추출(Stemming) / 표제어 추출(Lemmatization)

어간 추출과 표제어 추출은 하나의 단어로 일반화시켜서 문서 내의 단어 수를 줄이는 것이다.

표제어 추출은 단어들이 다른 형태를 가지더라도, 그 뿌리 단어를 찾아가서 단어의 개수를 줄이는 것이다. am, are, is는 서로 다른 스펠링이지만 원형은 be이다.

표제어 추출은 형태학적 파싱을 먼저 진행하는 것이 좋다. 형태소란 ‘의미를 가진 가장 작은 단위’를 뜻한다. 형태소에는 어간(stem)과 접사(affix)가 있다. *어간*은 `단어의 의미를 담고 있는 단어의 핵심 부분`이고 *접사*는 `단어에 추가적인 의미를 주는 부분`이다.

```python
# Stemming
from nltk.stem import PorterStemmer
ps = PorterStemmer()

stem_example1 = ["cook", "cooked", "cooking"]
ps_stem1 = [ps.stem(w) for w in stem_example1] #['cook', 'cook', 'cook']

from nltk.stem import LancasterStemmer
ls = LancasterStemmer()

stem_example2 = ["friend", "friends", "friendship", "friendships"]
ps_stem2 = [ps.stem(w) for w in stem_example2] #['friend', 'friend', 'friendship', 'friendship']
```

```bash
sudo python -m nltk.downloader -d /usr/local/share/nltk_data wordnet
```

```python
# Lemmatization
from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()
lem.lemmatize("is", pos="v") #be
lem.lemmatize("better", pos="a") #good
lem.lemmatize("friendship", pos="n") #
#n : 명사
#v : 동사
#a : 형용사
#r : 부사
```

## 정규 표현식을 사용한 토큰화

NLTK에서는 정규 표현식을 사용해서 단어 토큰화를 수행하는 RegexpTokenizer를 지원한다.

```python
import nltk
from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer("[\w]+")
print(tokenizer.tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop")) # ['Don', 't', 'be', 'fooled', 'by', 'the', 'dark', 'sounding', 'name', 'Mr', 'Jone', 's', 'Orphanage', 'is', 'as', 'cheery', 'as', 'cheery', 'goes', 'for', 'a', 'pastry', 'shop'] 
```

문자 또는 숫자가 1개 이상인 경우를 인식하는 코드이다. 따라서 문장에서 구두점을 제외하고, 단어들만을 가지고 토큰화를 수행하게 된다.

## 정수 인코딩(Integer Encoding)

컴퓨터는 텍스트보다는 숫자를 더 잘 처리 할 수 있습니다. 이를 위해 자연어 처리에서는 텍스트를 숫자로 바꾸는 여러가지 기법들이 있다.

Counter, keras, nltk의 FreqDist등 정수로 변환하는 방식이 다양하고 많은 module에서 지원한다.

### CountVectorizer

low당 단어 token의 빈도수를 구한다.

```python
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(lowercase=True, stop_words="english") # 대문자 -> 소문자, 영어 불용어를 제거하고 남은 단어들로 vector를 생성한다.
cv_reviews = cv.fit_transform(reviews)
cv_reviews.toarray() 
# array([[0, 0, 2, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
# [1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1]], dtype=int64)

u_words = cv.get_feature_names()
print(u_words)
# ['appetizer', 'barbecue', 'delicious', 'favor', 'food', 'great', 'just', 'korean', 'large', 'soho', 'steak', 'tables', 'tartare']
```

### TF-IDF Transform

low당 단어 token의 빈도수를 구한 후 단어의 가중치를 계산한다. 빈도수가 많은 단어의 가중치를 줄이고 빈도수가 적은 단어 가중치를 높게 계산한다. 

```txt
# tf: term frequency
# idf: inverse document-frequency

tf-idf(t, d) = tf(t, d) * idf(t)
```

```txt
# n: the total number of documents
# df(t): the document frequency of t
# if smooth_idf=False
idf(t) = log [ n / df(t) ] + 1 

# if smooth_idf=True - 제로 나누기를 방지한다.
idf(t) = log [ (1 + n) / (1 + df(t)) ] + 1
```

```python
tfidf1 = TfidfVectorizer(lowercase= True, stop_words=new_stopwords, ngram_range = (1,2)).build_analyzer()
def tfidf_stem(x):
    return(ps.stem(w) for w in tfidf1(x))
tfidf_stem_vertorizer = TfidfVectorizer(analyzer=tfidf_stem)
tfidf_reviews = tfidf2.fit_transform(reviews)
tfidf_u_words = tfidf2.get_feature_names()
pd.DataFrame(tfidf_reviews.toarray(),columns=tfidf_u_words)
```

`ngram_range`는 n-gram은 n개의 연속적인 단어 나열을 의미한다. [참고](https://wikidocs.net/21692)


## Reference
* [1) 토큰화(Tokenization) - 딥 러닝을 이용한 자연어 처리 입문](https://wikidocs.net/21698)
