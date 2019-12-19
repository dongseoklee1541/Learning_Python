# CH.4 Functions, the Building Blocks of Code

## The global and nonlocal statements

함수를 선언한뒤 함수 속에서 선언되는 변수들은 모두 지역변수로, 함수의 블록을 벗어나면 
소멸된다.

```python
def A():
    x = 10        # A의 지역 변수 x
    def B():
        x = 20    # x에 20 할당
 
    B()
    print(x)      # A의 지역 변수 x 출력
 
A()
```
물론 위와 같이, 같은 이름으로 생성하더라도 영향을 끼치지 못한다.
```
10
```

그렇다면 B()에서 A()에 선언된 변수를 바꾸고 싶다면 어떻게 해야 할까. **nonlocal** 을 사용해야 한다.

```python
def A():
    x = 10        # A의 지역 변수 x
    def B():
        nonlocal x    # 현재 함수의 바깥쪽에 있는 지역 변수 사용
        x = 20        # A의 지역 변수 x에 20 할당
 
    B()
    print(x)      # A의 지역 변수 x 출력
 
A()
```
```
20
```
이렇듯 B() 함수에서 수정한 x의 값이 A()에 적용되었다.

마찬가지로 nonlocal처럼 **global** 을 사용하면 전역변수도 수정할 수 있다.

```python

# Argument passing
>>> x = 3
>>> def func(y):
	print(y)

>>> func(x)
3 # x의 값이 나온다.

# Assignment to argument names don't affect the caller
>>> x = 3
>>> def func(x):
	x = 7 # 여기서 선언한 x는 func 안의 지역변수에 불과해, 전역변수 x에 영향을 끼치지 못함

>>> func(x)
>>> print(x)
3

# Changing a mutable affects the caller

>>> x = [1, 2, 3]
>>> def func(x):
	x[1] = 42 # caller 의 값을 바꾼다, x를 바꾸는게 아니라 x[1]의 주소에 접근해서 바꾸는 것
              # x를 새로 만드는 것이 아니다!
    
>>> func(x)
>>> print(x)
[1, 42, 3]

# How to specify input parameters

# Positional arguments
>>> def func(a,b,c):
	print(a,b,c)

>>> func(1,2,3)
1 2 3

# Keyword arguments and default values
# Keyword arguments are assigned by keyword using the name=value syntax.

>>> def func(a,b,c):
	print(a,b,c)

>>> func(a=1,c=2,b=3)
1 3 2

# second ex
>>> def func(a,b=4,c=88):
	print(a,b,c)
>>> func(1) # a의 위치에 바로 들어가고
1 4 88
>>> func(b=5,a=7,c=9) # 순서를 바꿔서 넣어도 들어간다.
7 5 9
>>> func(42,c=9) 
42 4 9

# Variable positional arguments

>>> def minimum(*n): # 매개변수를 튜플로 만들겠다.
	if n:
		mn = n[0]
		for value in n[1:]:
			if value < mn: # value가 값이 비어있지 않으면 True를 반환, 비어있으면 False
				mn = value
		print(mn)

>>> minimum(1,3,-7,9) # n = (1,3,-7,9) 로 이루어진 튜플
-7
>>> minimum
<function minimum at 0x0154D618>
>>> minimum() # 아무것도 나오지 않는다.

# 매개변수에서의 *, 인자에서의 *의 차이점
>>> def func(*args):
	print(args)

>>> values = (1,3,-7,9)
>>> func(values)
((1, 3, -7, 9),)
>>> func(*values) # * : unpacking, values의 튜플들을 다 빼내겠다.
(1, 3, -7, 9)

# Variable keyword arguments

>>> def func(**kwargs): # **kwargs : dict 형으로 받는 매개변수
	print(kwargs)

>>> func(a=1,b=42)  # 사전형으로 보내고
{'a': 1, 'b': 42}
>>> func(**{'a':1,'b':42}) # 사전형을 풀어서 보내고
{'a': 1, 'b': 42}
>>> func(**dict(a=1,b=42)) # 똑같이 사전형을 풀어서 보낸다.
{'a': 1, 'b': 42}

# 이러한 방식의 중요성은 DB에 연동할때 많이 나타난다.
>>> def connect(**options):
	conn_params = {
 'host': options.get('host', '127.0.0.1'), # default 값을 정하는 get과
 'port': options.get('port', 5432),
 'user': options.get('user', ''),
 'pwd': options.get('pwd', ''),}
	print(conn_params)
    
>>> connect()
{'host': '127.0.0.1', 'port': 5432, 'user': '', 'pwd': ''}
>>> connect(host='127.0.0.42', port=5433)
{'host': '127.0.0.42', 'port': 5433, 'user': '', 'pwd': ''}
>>> connect(port=5431, user = 'fab', pwd = 'gandalf')
{'host': '127.0.0.1', 'port': 5431, 'user': 'fab', 'pwd': 'gandalf'}

# Keyword-only arguments
# 매개변수를 지정해줘야 하는 것들은 해줘야 한다. *의 위치를 주의하라. 얘가 다 받아먹을 수 있다.

>>> def kwo(*a, c):
	print(a,c)

>>> kwo(1,2,3,c=7)
(1, 2, 3) 7
>>> kwo(c=4)
() 4
>>> kwo(1,2)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    kwo(1,2)
TypeError: kwo() missing 1 required keyword-only argument: 'c'

>>> def kwo2 (a, b=42, *, c):
	print(a,b,c)

>>> kwo2(3,b=7,c=99)
3 7 99
>>> kwo2(3,c=13)
3 42 13
>>> kwo2(3,23)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    kwo2(3,23)
TypeError: kwo2() missing 1 required keyword-only argument: 'c'

# Combining input parameters

>>> def func(a,b,c=7,*args,**kwargs):
	print('a,b,c:',a,b,c)
	print('args:',args)
	print('kwargs:',kwargs)

>>> func(1, 2, 3, *(5, 7, 9), **{'A': 'a', 'B': 'b'}) #
a,b,c: 1 2 3
args: (5, 7, 9)
kwargs: {'A': 'a', 'B': 'b'}
>>> func(1, 2, 3, 5, 7, 9, A='a', B='b') # 위와 동일한 결과
a,b,c: 1 2 3
args: (5, 7, 9)
kwargs: {'A': 'a', 'B': 'b'}

#ex2
>>> def func_with_kwonly(a, b=42, *args, c, d=256, **kwargs):
	print('a,b:',a,b)
	print('c,d:',c,d)
	print('args:',args)
	print('kwargs:',kwargs)

>>> func_with_kwonly(3, 42, c=0, d=1, *(7, 9, 11), e='E', f='F')
a,b: 3 42
c,d: 0 1
args: (7, 9, 11)
kwargs: {'e': 'E', 'f': 'F'}
>>> func_with_kwonly(3, 42, *(7, 9, 11), c=0, d=1, e='E', f='F') # 순서를 섞어도 입력만 잘해주면 됨
a,b: 3 42
c,d: 0 1
args: (7, 9, 11)
kwargs: {'e': 'E', 'f': 'F'}

# Avoid the trap! Mutable defaults

>>> def func(a=[],b={}):
	print(a)
	print(b)
	print('#'*12)
	a.append(len(a))
	b[len(a)] = len(a)
>>> func()
[]
{}
############
>>> func()
[0]
{1: 1}
############
>>> func()
[0, 1]
{1: 1, 2: 2}
############

>>> func()
[0, 1, 2]
{1: 1, 2: 2, 3: 3}
############
>>> func(a=[1, 2, 3], b={'B': 1})
[1, 2, 3]
{'B': 1}
############
>>> func()
[0, 1, 2, 3]
{1: 1, 2: 2, 3: 3, 4: 4}
############

# func이 반복되면서 a가 기본값이 안되고 누적되는걸 막고 싶다면,
>>> def func(a=None):
	if a is None:
		a = [] # 이렇게 하면 a는 계속 초기화 된다.
        
# Return values

>>> def factorial(n):
	if n in (0,1):
		return 1
	result = n
	for k in range(2,n):
		result *= k
	return result

>>> f5 = factorial(5)
>>> f5
120

# 하지만 파이썬에선 팩토리알을 더 쉽게 해주는 모듈들이 존재한다.
>>> from functools import reduce
>>> from operator import mul
>>> def factorial(n):
	return reduce(mul,range(1,n+1),1) # mul : 곱하기 
                                      #reduce(function, iterable, initializer) : 함수,반복,시작
>>> f5 = factorial(5)
>>> f5
120


# Returning multiple values
# 파이썬에서 여러개의 값을 리턴한다면 튜플을 사용하는 것이 좋다.

>>> def moddiv(a,b):
	return a//b , a % b

>>> print(moddiv(20,7))
(2, 6)

# Functions shouldn't have side effects

>>> numbers = [4, 1, 7, 5]
>>> sorted(numbers) # 원래의 numbers의 값은 변하지 않는다. 리턴값일 뿐
[1, 4, 5, 7]
>>> numbers # let's verify
[4, 1, 7, 5] # good, untouched
>>> numbers.sort() # 하지만 이는 numbers의 메서드일 뿐이라 numbers의 값을 바꾼다.
>>> numbers
[1, 4, 5, 7]

# Recursive functions

>>> def factorial(n):
	if n in (0,1): # python 스타일의 0,1 확인 n == 0 | n == 1 이런 방식이 아니라.
		return 1
	return factorial(n-1)*n

>>> f = factorial(10)
>>> f
3628800

# Anonymous functions

>>> def is_multiple_of_five(n):
	return not n % 5

>>> def get_multiples_of_five(n):
	return list(filter(is_multiple_of_five, range(n)))

>>> print(get_multiples_of_five(50))
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45]

# is_multiple_of_five과 같은 간단한 함수는
# lambda 함수를 사용하여 더 간결하게 만들 수 있다.
# filter() : list, dict 과 같은 iterable 한 데이터를 특정 조건이 일치하는 값만 추출해 낼때 사용하는 함수
>>> def get_multiples_of_five(n):
	return list(filter(lambda k: not k % 5, range(n)))

>>> print(get_multiples_of_five(50))
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45]

# 함수를 람다 함수로 바꾼 예

>>> def adder(a,b):
	return a+b
>>> adder_lambda = lambda a,b: a+b

>>> def to_upper(s):
	return s.upper()
>>> to_upper_lambda = lambda s: s.upper()

# Function attributes
# getattr : 이름의 속성들을 꺼낼 수 있는 Build-in 함수
# getattr(object, name[, default])

for attribute in special_attributes:
	print(attribute, '->', getattr(multiplication, attribute))

	
__doc__ -> Return a multiplied by b.
__name__ -> multiplication
__qualname__ -> multiplication
__module__ -> __main__
__defaults__ -> (1,)
_code__ -> <code object multiplication at 0x00C303E8,

```
