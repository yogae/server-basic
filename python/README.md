# python class

함수뿐만 아니라 다양한 변수를 포함한 큰 프로그램을 하나의 묶음으로 정의하는 것이 "클래스(class)"이다. 클래스의 기본적인 사용법부터 설명한다.

## class 작성

```python
class CustomClass:
    def __init__(self, param):
```

`__init__` method는 class를 초기화 시킬때 호출된다.

## 사용

```python
class CustomClass:
    def __init__(self, a, b):
        self._a = a
        self._b = b


custom_class = CustomClass(1, 2) # 초기화
```

## Reference

* [https://araikuma.tistory.com/371]
