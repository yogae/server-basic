# nltk(Natural Language Toolkit)

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

## [preprocessing](./preprocessing)

## [modeling](./modeling)