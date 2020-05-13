# nltk(Natural Language Toolkit)
#python/nlp

python에서 자연어 처리에 많이 사용하는 nltk를 사용해보았다. 

## install
pip로 nltk를 설치한다.

```bash
pip install nltk
pip install numpy
```

nltk는 pip로만 설치하여 사용할 수 없다. nltk에서 datasets/models는 따로 설치하고 되어있다. 파이썬 셸에서 `ntlk.download()` 함수를 실행하여 UI를 사용하여 설치할 추가 패키지를 선택할 수 있다. 명령어를 사용하는 것이 편해서 아래의 명령어를 사용하여 설치했다.

```bash
sudo python -m nltk.downloader -d /usr/local/share/nltk_data "<pakage 이름>"
```

`/usr/local/share/nltk_data`는 mac에서 nltk 패키지가 저장되는 위치이다. 다른 os를 사용하는 경우 [Installing NLTK Data — NLTK 3.5 documentation](http://www.nltk.org/data.html#interactive-installer)를 참고해라. 사용할 nltk pakage만 위의 명령어를 사용하여 설치할 수 있다. 사용할 nltk pakage가 확실하지 않다면 `popular`를 사용한다.

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




## Reference
* [1) 토큰화(Tokenization) - 딥 러닝을 이용한 자연어 처리 입문](https://wikidocs.net/21698)
