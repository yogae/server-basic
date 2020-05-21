# modeling

## data 나누기

머신러닝 모델을 학습하고 그 결과를 검증하기 위해서는 원래의 데이터를 Training, Validation, Testing의 용도로 나누어 다뤄야 한다. 모델이 내가 가진 학습 데이터에 너무 과적합되도록 학습한디면 조금이라도 벗어난 케이스에 대해서는 예측율이 현저히 떨어지게 된다(Overfitting).

```python
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(tfidf_review, mist_review["Overall"], test_size = 0.3, random_state=0)
```

train_test_split의 parameter는 아래와 같다.

* test_size: test data 사이즈
* train_size: train data 사이즈
* shuffle: data를 random하게 섞는다.
* random_state: shuffle이 False일 사용되지 않는다. shuffle이 True인 경우 shuffle되는 규칙을 저장하여 다시 실행하여도 같은 규칙으로 shuffle이 진행되도록 한다. [참고](https://stackoverflow.com/questions/58955816/difference-between-shuffle-and-random-state-in-train-test-split)

## 예측

### Logistic Regression

Logistic Regression은 사건의 발생 가능성을 예측할 때 사용되는 통계기법이다. logistic regression 은 데이터가 두 집단(0또는 1)로 나뉘어져 있는 경우에 사용된다.

```python
from sklearn.linear_model import LogisticRegression

LR = LogisticRegression()
LR.fit(x_train, y_train)
y_pred=LR.predict(x_test)
```

## 평가

```python
from sklearn.metrics import accuracy_score

accuracy_score(y_pred, y_test)
```
