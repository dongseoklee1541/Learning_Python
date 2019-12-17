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

## Reals
파이썬은 IEEE 754 부동소수점을 double-precision(64 bits)만을 사용한다.

## Complex numbers(복소수)
파이썬은 복소수를 지원한다. 프로그래밍에서는 i를 j로 표기한다.

```python
c = 3.14 + 2.73j # 2.73 이 imaginary 부분이다.

c.read # real part
# 3.14
c.imag # imaginary part
# 2.73

c.conjugate() # conjugate of A + Bj is A - Bj
# (3.14-2.73j)

c * 2 # 곱셈도 가능하다.
# (6.28+5.46j)
c ** 2 # 제곱도 가능
# (2.4067000000000007+17.1444j) 

d = 1 + 1j # 덧셈 뺄셈도 가능하다.
c - d 
# (2.14+1.73j)
```

## Fractions and decimals (분수와 십진수)

```python
from fractions import Fraction

Fraction(10,6) 
# Fraction(5,3) # 분모와 분자를 서로 나눠 가장 작은 수로 만들어준다.

Fraciton(1,3) + Fraction(2,3) # 1/3 + 2/3 = 3/3 = 1/1
# Fraction(1,1)

f = Fraction(10,6)
f.numberator
# 5
f.denominator
# 3
```

decimals 은 부동소수점을 사용하는 수가 아니라 십진수를 사용하기에 소수 표현이 더 정확하다.

```python

from decimal import Decimal as D

D(3.14) # 그냥 숫자로 표기할 경우 부동소수점으로 나타낸다.
# Decimal('3,140000000000000124344978758017532527446746826171875')

D('3.14') # string으로 사용해야 십진수로 사용 할 수 있다.
# Decimal('3.14')

D('0.1') * D(3) - D('0.3') # string 으로 사용한다면
#Decimal('0.0') 으로 정확하게 계산된다.
```

## Immutable sequences
strings, tuples, and bytes 등이 존재한다.

### Strings and byte

파이썬은 문자열이 기본적으로 unicode 로 인코딩 되어 있고, 본인이 사용하기 적합한 포멧으로 인코딩해서 사용하면 된다.
또한 문자열을 사용하는데 있어서, `string`, "string" , ```string``` , """string""" 등 여러가지 방식으로 

표현 할 수 있다. 이는 문자열을 다양한 방식으로 만들기 위해서이다.

```python
str1 = 'this is a string.'

str2 = "this is also a string."

str3 = ```this is string.
using triple qutoes.```

str4 = """This is too
is a multiline"""

len(str1) # 문자열의 길이도 존재한다.
# 17 
```

### Encoding and decoding strings

encode/decode 메서드를 사용해서 unicode strings 을 byte objects 로 decode 할 수 있다. 

```python

s = "This is üŋíc0de" 
type(s)
# <class 'str'>

encoded_s = s.encode('utf-8')
encoded_s
# b'This is \xc3\xbc\xc5\x8b\xc3\xadc0de' 
type(encoded_s)
# <class 'bytes'>

encoded_s.decode('utf-8')
# 'This is üŋíc0de'

bytes_obj = b"A bytes object" # 문자열 앞에 b를 붙여주면
type(bytes_obj)
# <class 'bytes'> , byte 형으로 나온다.
```

### Indexing and slicing strings

Immutable 한 문자열을 잘라서 일부만 사용 할 수 있다. 물론 Immutable 한 형태이기에 읽기 전용이다.

```python

s = "The trouble is you think you have time."
s[0] # incdexing, 첫번째 char를 읽어라.
# 'T'
s[5]
# 'r'

s[:4] # slicing, 여기까지 읽어라.
# 'The '

s[4:] # 4번에서부터 끝까지 읽어라.
# 'trouble is you think you have time.'

s[2:14:3] # slicing, start, stop and step (3 단위의 chars)
# 'erb '
```

### Tuples

```python

t = ()
type(t)
# <class 'tuple'>

a, b, c = 1, 2, 3 
a, b, c
# (1, 2, 3) tuples 로 나온다.

a, b = 2, 1
a, b = b, a # python 의 swap 방식
a,b
# (1,2)

```

## Mutable sequences

선언 후 값을 바꿀 수 있는 types 은 list 와 byte arrays가 있다. 

### Lists

Tuples 과 비슷하지만, Lists 는 값을 변경할 수 있다.

```python

list((1,3,5,7,9)) # tuple 을 list로 바꾸기
# [1, 3, 5, 7, 9]

list('hello') # string 을 list로
# ['h','e','l','l','o']

a = [1, 2, 1, 3]
a.append(13)
a
# [1, 2, 1, 3, 13] list 의 끝에 추가

a.count(1) # 첫번째 index 읽어오기
# 2

a.index(13)
# 4

a.insert(0,17) # 0번 index에 17 넣기
a
# [17, 1, 2, 1, 3, 13, 5, 7]

a.pop() # 맨 마지막 index의 값 출력하고 빼기 
# 7
a.pop(3) # 3번째 index 값 출력하고 빼기
# 1

a
# [17, 1, 2, 3, 13, 5] 

a.remove(17)  # 17을 찾아서 지워라
a
# [1, 2, 3, 13, 5]

a.reverse() # list의 값들의 순서를 바꾸기
a
# [5, 13, 3, 2, 1]

a.sort() # 오름차순 정렬
a
# [1, 2, 3, 5, 13]

a.clear() # 값들 모두 제거
a
# [] 

```

lists 는 다양한 형식도 함께 묶어서 받을 수 있다.

```python

>>> a = list('hello')
>>> a
['h', 'e', 'l', 'l', 'o']
>>> a.append(100)
>>> a
['h', 'e', 'l', 'l', 'o', 100]
>>> a.extend((1,2,3))
>>> a
['h', 'e', 'l', 'l', 'o', 100, 1, 2, 3]
>>> a.extend('...')
>>> a
['h', 'e', 'l', 'l', 'o', 100, 1, 2, 3, '.', '.', '.']

```

list는 최대,최소,합,길이를 알 수 있는 메서드들도 존재한다.

```python

>>> a = [1, 3, 5, 7] 
>>> min(a)  # min
1 
>>> max(a)  # maximum 
7 
>>> sum(a)  # sum 
16 
>>> len(a)  # 리스트의 길이
4 
>>> b = [6, 7, 8] 
>>> a + b # 리스트에서 "+"는 리스트끼리 서로 연결하는 것 
[1, 3, 5, 7, 6, 7, 8]
>>> a * 2 # 곱셈은 반복
[1, 3, 5, 7, 1, 3, 5, 7]
```

list 는 또한 tuple의 배열을 바꿀 수 있다.

* sorted(arg) : 매개변수의 값들을 정렬해주는 메서드, sort는 매개변수가 없다.

```python

>>> from operator import itemgetter
>>> a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]
>>> sorted(a) 
[(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
>>> sorted(a,key=itemgetter(0)) # 그냥 sorted 와 같은 방법으로 배열이 진행됨
[(1, 3), (1, 2), (2, -1), (4, 9), (5, 3)]
>>> sorted(a, key=itemgetter(0,1)) # 인덱스의 0,1 을 모두 고려하여 정렬
[(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
>>> sorted(a,key=itemgetter(1)) # 인덱스 1만 고려하여 정렬
[(2, -1), (1, 2), (5, 3), (1, 3), (4, 9)]
>>> sorted(a,key=itemgetter(1),reverse=True) # 인덱스 1과 내림차순 정렬
[(4, 9), (5, 3), (1, 3), (1, 2), (2, -1)]

```

### Byte arrays

바이트 배열은 byte와 마찬가지로 binary data 를 다루는데, bytes 는 1바이트 단위로 값을 연속적으로 저장하는 시퀸스이다(0~255,0x00~0xFF 까지 사용)

```python

>>> bytearray()
bytearray(b'')
>>> bytearray(10) # 값이 0인 byte 배열 10개 생성
bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
>>> bytearray(range(5)) # 0~4까지의 값을 가진 바이트 배열 5개 생성
bytearray(b'\x00\x01\x02\x03\x04')
>>> name = bytearray(b'Lina') 
>>> name.replace(b'L',b'l') # L을 l 로 변경
bytearray(b'lina')
>>> name.endswith(b'na') # 끝의 문자가 na 야?
True
>>> name.upper()
bytearray(b'LINA')
>>> name.count(b'L')
1

```

### Set type

파이썬에는 집합형이 존재하는데, set 과 frozenset 두가지가 존재한다. set 은 값 변경이 가능하지만, frozenset 은 값을 변경할 수도, 순서도 없다.

#### set

```python

>>> small_primes = set() # 집합 선언
>>> small_primes.add(2) # 원소 추가
>>> small_primes.add(3)
>>> small_primes.add(5)
>>> small_primes
{2, 3, 5}

>>> small_primes.add(1)
>>> small_primes
{1, 2, 3, 5}
>>> small_primes.remove(1)
>>> 3 in small_primes
True
>>> 4 in small_primes
False
>>> 4 not in small_primes
True
>>> small_primes.add(3)
>>> small_primes
{2, 3, 5} # 중복은 허용되지 않는다.

>>> bigger_primes = set([5,7,11,13])
>>> small_primes | bigger_primes # "|" 은 합집합
{2, 3, 5, 7, 11, 13}
>>> small_primes & bigger_primes # "&" 은 교집합
{5}
>>> small_primes - bigger_primes # "-" 은 차집합
{2, 3}
```

#### forzenset
frozenset 은 불변형이므로 add, remove 는 사용할 수 없다. 하지만 합집합,공집합,차집합 등은 가능하다.

```python

>>> small_primes = frozenset([2,3,5,7])
>>> bigger_primes = frozenset([5,7,11])
>>> small_primes.add(11)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    small_primes.add(11)
AttributeError: 'frozenset' object has no attribute 'add'
>>> small_primes.remove(2)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    small_primes.remove(2)
AttributeError: 'frozenset' object has no attribute 'remove'
>>> small_primes & bigger_primes
frozenset({5, 7})

```

### Mapping types – dictionaries 

사전형은 key값과 values 가 매칭되어야 하는 형식이다. key 값의 중복은 허용하지 않으며 mutable 형식이다.

values 의 경우 모든 형태의 자료형을 사용 할 수 있다.


{"A" : 1 , "Z" : -1}을 다섯가지의 다른 방식으로 만들어 보겠다.
```python
>>> a = dict(A=1,Z=-1)
>>> b = {'A' : 1, 'Z':-1}
>>> c = dict(zip(['A','Z'],[1,-1]))
>>> d = dict([('A',1),('Z',-1)])
>>> e = dict({'Z':-1,'A':1})
>>> a == b == c == d == e
True
```

* zip() : 매개변수로 받은 쌍을 하나의 object로 만들어 준다.
```python
>>> list(zip(['h','e','l','l','o'],[1,2,3,4,5]))
[('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5)]
>>> list(zip('hello',range(1,6))) ## 더 pythonic 답다.
[('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5)]
```

사전형을 만드는 방법을 더 자세히 알아보자. 

```python

>>> d = {}
>>> d['a'] = 1 # key 와 value 추가
>>> d['b'] = 2
>>> len(d) # 짝 몇개야?
2
>>> d['a'] # a의 value는 무엇?
1
>>> d # d는 어떻게 생겼니
{'a': 1, 'b': 2}
>>> del d['a'] # key 'a'를 지워
>>> d
{'b': 2}
>>> d['c'] = 3
>>> 'c' in d # key 'c' 가 있나요?
True
>>> 3 in d # value 값을 찾아주진 않아요
False
>>> 'e' in d
False
>>> d.clear() # 값을 모두 다 지워주세요.
>>> d
{}

```

