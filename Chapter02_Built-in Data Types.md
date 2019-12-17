# CH.2 Built-in Data Types

컴퓨터에서 다루는 모든것은 data로 이루어져있다. 데이터는 여러가지 형태로 이루어져 있다. 파이썬에서 Object 는 데이터의 추상화이며 다양한 데이터 구조를
가지고 있다.

## Mutable or immutable? That is the question 

값이 변할 수 있다면, Mutable 없다면 immutable 이라고 한다. 파이썬에서 int 는 immutable 한 값이다.

```python
age = 42
age
# 42
age = 43 # A
age
# 43
```
하지만 여기선 int 형인 age가 42에서 43으로 바뀌는것을 볼 수있는데, 이것은 새로운 age를 만들어 43을 가르키고 있기 때문이지 값이 변한 것은 아니다.

```python
age = 42 
id(age) 
# 456352 
age = 43 
id(age) 
# 456384 
# 와 같이 id의 주소가 다르다.
```

Mutable 한 타입은 **커스텀 클래스** 인 경우이다.

```python
fab = Person(age=39)
fab.age
# 39
id(fab)
# 139632387887456
fab.age = 29
id(fab)
# 139632387887456
# id의 주소가 같다.
```

## Numbers
파이썬에서 integers 의 길이는 메모리가 허용하는 한 무한하다. 사칙연산도 가능한데 integers 의 특징으로 **true division(/)** 과 
**intger division(//)** 이 있다.

```python
7 / 4 # true division
# 1.75 로 실수 형태로 반환 해주는 반면

7 // 4 # integer division은 소수 부분을 버린다.
# 1

-7 // 4 # 파이썬은 음수로도 무한하므로 -1이 아닌 -2를 반환한다.
# -2 

int(-1.75) # 소수 부분을 버리고 싶다면, 내장함수인 int를 사용하자.
# -1 
```

## Booleans
불리언 자료형은 true 와 false로 이루어진 대수의 부분집합이다. 불리언은 또한 intgers의 서브클래스이기도 하다.

```python
int(True) # True는 1
# 1
int(False) # False 는 0
# 0

bool(1) # 0 외의 값은 모두 True 이다
# True
bool(42)
# True
bool(0)
# False

not True # 또한 연산자(operators , and, or , not)로도 사용된다.
# False
not False
# True
```

또한 불리언은 intgers의 부분 클래스로 사칙연산도 가능하다.
```python
1 + True
# 2

False + 42
# 42
```

