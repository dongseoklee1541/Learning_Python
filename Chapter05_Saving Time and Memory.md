```python
# map,zip and filter

# map 

""" 
map은 기존의 리스트를 바꾸지 않고, 지정된 함수로 리스트의 요소를 변경하는 함수이다.
list(map(함수,리스트))
tuple(map(함수,튜플))
"""

# list로 만드는 map
>>> map(lambda *a: a, range(3))
<map object at 0x00C1AFF0>
>>> list(map(lambda *a: a, range(3)))
[(0,), (1,), (2,)]
>>> list(map(lambda *a: a, range(3), 'abc'))
[(0, 'a'), (1, 'b'), (2, 'c')]
>>> list(map(lambda *a: a, range(3), 'abc',range(4,7)))
[(0, 'a', 4), (1, 'b', 5), (2, 'c', 6)]

# map은 iterator 가 짧으면 실행을 멈춘다.

>>> list(map(lambda *a: a, (), 'abc')) #  튜플 이 abc보다 짧고
[]
>>> list(map(lambda *a: a, (1,2), 'abc')) # 위와 동일
[(1, 'a'), (2, 'b')]
>>> list(map(lambda *a: a, (1, 2, 3, 4), 'abc')) # 'abc'가 튜플보다 짧다
[(1, 'a'), (2, 'b'), (3, 'c')]

""" 
학생들의 점수를 내림차순으로 정렬하고 싶다. 두개의 함수를 이용해서 만들어보자.
"""

students = [
 dict(id=0, credits=dict(math=9, physics=6, history=7)),
 dict(id=1, credits=dict(math=6, physics=7, latin=10)),
 dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
 dict(id=3, credits=dict(math=5, physics=5, geography=7)),]
 
def decorate(student):
# create a 2-tuple (sum of credits, student) from student dict
	return (sum(student['creadits'].values()),student)
  
def undecorate(decorated_student):
# discard sum of credits, return original student dict
	return decorated_student[1]
  
students = sorted(map(decorate,students), reverse=True)
# 총합과 합이 높은 순으로 졍렬(내림차순)
[(27, {'id': 2, 'credits': {'history': 8, 'physics': 9, 'chemistry': 10}}), (23, {'id': 1, 'credits': {'math': 6, 'physics': 7, 'latin': 10}}), (22, {'id': 0, 'credits': {'math': 9, 'physics': 6, 'history': 7}}), (17, {'id': 3, 'credits': {'math': 5, 'physics': 5, 'geography': 7}})]

students = list(map(undecorate, students))
# 총합 제거 후 원래의 양식으로 돌림, 순서는 그대로
[{'id': 2, 'credits': {'history': 8, 'physics': 9, 'chemistry': 10}}, {'id': 1, 'credits': {'math': 6, 'physics': 7, 'latin': 10}}, {'id': 0, 'credits': {'math': 9, 'physics': 6, 'history': 7}}, {'id': 3, 'credits': {'math': 5, 'physics': 5, 'geography': 7}}]


#zip

# zip 과 map 똑같은 결과를 만들어 내기
>>> grades = [18, 23, 30, 27, 15, 9, 22]
>>> avgs = [22, 21, 29, 24, 18, 18, 24]
>>> list(zip(avgs, grades))
[(22, 18), (21, 23), (29, 30), (24, 27), (18, 15), (18, 9), (24, 22)]
>>> list(map(lambda *a: a, avgs, grades))
[(22, 18), (21, 23), (29, 30), (24, 27), (18, 15), (18, 9), (24, 22)]

"""
zip 과 map을 효과적으로 같이 사용할 수 있는 경우는, list 간에 가장 큰 값을 비교하여 넣고
리스트로 만드는 것이다.
"""
>>> a = [5, 9, 2, 4, 7]
>>> b = [3, 7, 1, 9, 2]
>>> c = [6, 8, 0, 5, 3]
>>> maxs = map(lambda n: max(*n), zip(a,b,c))
>>> maxs
<map object at 0x00C31990>
>>> list(maxs)
[6, 9, 2, 9, 7]

# filter
"""
 filter 함수는 built-in 함수로 list 나 dictionary 같은 iterable 한 데이터를 특정 조건에 일치하는 값만 추출해 낼때 사용하는 함수이다.
"""
# func 도 쓸 수 있지만, lambda식을 통해 더 간결하게 쓸 수 있다.
>>> test = [2,5,8,0,0,1,0]
>>> list(filter(None,test))
[2, 5, 8, 1]
>>> list(filter(lambda x:x, test))
[2, 5, 8, 1]
>>> list(filter(lambda x:x >4, test))
[5, 8]

# Comprehensions
"""
list,dict and sets 등 다른 타입들에 대한 이해가 필요, list를 먼저 시작해보자.
0부터 9까지의 제곱의 리스트를 어떻게 만들까?
"""
>>> squares = []
>>> for n in range(10):
	squares.append(n ** 2)

>>> list(squares)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 또는 map을 활용해서 더 짧게 만들 수 있다.

>>> squares = []
>>> squares = map(lambda x:x**2, range(10))
>>> list(squares)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 그냥 한줄로도 가능
>>> [n** 2 for n in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# filter,map 를 사용한 list 이해
""" 0~9 사이의 제곱 수 중 2로 나누어 떨어지는숫자는?"""
>>> sql = list(filter(lambda n : not n % 2, map(lambda n:n **2, range(10)))) #filter 와 map
>>> sql2 = [n ** 2 for n in range(10) if not n % 2]
>>> print(sql, sql == sql2)
[0, 4, 16, 36, 64] True

# Nested comprehensions
"""
중첩된 것들의 이해
"""

>>> items = 'ABCDE'
>>> pairs = []
>>> for a in range(len(items)):
	for b in range(a,len(items)):
		pairs.append((items[a],items[b]))

>>> pairs
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'C'), ('C', 'D'), ('C', 'E'), ('D', 'D'), ('D', 'E'), ('E', 'E')]

# 위와 동일하지만 코드는 짧다.
>>> items = 'ABCDE'
>>> pairs = [(items[a], items[b]) for a in range(len(items)) for b in range(a,len(items))]

# Filtering a comprehension

""" 필터로 피타고라스 계산을 하고, c의 값이 정수인 것만 찾아보자. """
>>> from math import sqrt
>>> mx = 10
>>> legs = [(a,b,sqrt(a**2 + b**2))
	for a in range(1,mx) for b in range(a, mx)] # sqrt(a^2 + b^2) = sqrt(c^2)
>>> legs = list(filter(lambda triple: triple[2].is_integer(), legs)) # c 값이 정수인 것만 가져오기
>>> print(legs)
[(3, 4, 5.0), (6, 8, 10.0)]

# 위와 같은 결과에서 세번째 값이 실수로 나오는 것을 정수형으로 바꾸자.
>>> legs = list(
	map(lambda triple: triple[:2] + (int(triple[2]),),legs)) 
  # map을 통해 0,1 인덱스의 값과 2번째 인덱스의 값을 합쳐 튜플로 만들었다.
>>> print(legs)
[(3, 4, 5), (6, 8, 10)]

# map 없이 더 간단하게 하는 방법은?
>>> mx = 10
>>> legs = [(a,b,sqrt(a**2 + b**2))
	for a in range(1,mx) for b in range(a, mx)]
>>> legs = [(a,b,int(c)) for a,b,c in legs if c.is_integer()]
# c를 legs에 넣을때 int로 변환해서 넣자.
>>> print(legs)
[(3, 4, 5), (6, 8, 10)]

# dict comprehensions
""" list 와 dict 은 비슷하게 사용하면 되지만, 문법이 약간 다르다. """

>>> from string import ascii_lowercase
>>> lettermap = dict((c,k) for k, c in enumerate(ascii_lowercase,1))

>>> lettermap = {c:k for k,c in enumerate(ascii_lowercase,1)} # dict을 key : values로 바꿔서 저장

""" 사전형은 key 값에 중복을 허용하지 않는다. 중복으로 입력되더라도 에러 없이 가장 나중에 입력된
값으로 저장이 된다. """

>>> word = 'Hello'
>>> swaps = {c: c.swapcase() for c in word}
>>> print(swaps)
{'H': 'h', 'e': 'E', 'l': 'L', 'o': 'O'}
>>> positions = {c:k for k, c in enumerate(word)}
>>> print(positions)
{'H': 0, 'e': 1, 'l': 3, 'o': 4} # 'l' : 2 가 아니라 3인 것은, 2의 'l'을 나중에 덧씌운 값이기 때문

#set comprehensions
""" 파이썬은 set() 과 {} 로 집합을 만들 수 있다. """
>>> word = 'Hello'
>>> letters1 = set(c for c in word)
>>> letters2 = {c for c in word}
>>> print(letters1)
{'o', 'l', 'H', 'e'}
>>> print(letters1 == letters2)
True

# Generators 
""" Generator는 functions 과 expressions이 존재한다. """

# Generator functions
"""
제네레이터 함수는, 실행되어 한번에 값을 리턴하는게 아니라 호출될때마다 yield를 통하여 하나씩 반환하는
역할을 한다. 호출되고 난뒤 다시 호출될때까지 기다리고 있다가 호출이 된다면 그때 갖고 있는 값을 반환하는
녀석들이다.
"""

>>> def get_squares(n): # 일반 함수
	return [x ** 2 for x in range(n)]

>>> print(get_squares(10))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> def get_squares_gen(n): # 제네레이터 함수
	for x in range(n):
		yield x ** 2

>>> print(list(get_squares_gen(10)))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 여기까진 차이가 없다.

>>> def get_squares_gen(n):
	for x in range(n):
		yield x ** 2

>>> squares = get_squares_gen(4)
>>> print(squares) # 한번에 값을 반환하지 않는다. 기다리고 있는 상태.
<generator object get_squares_gen at 0x00BF1F30>
>>> print(next(squares)) # next로 호출 될때마다 값을 반환
0
>>> print(next(squares))
1
>>> print(next(squares))
4
>>> print(next(squares))
9
>>> print(next(squares))
Traceback (most recent call last): # for  loop 에서 반복이 끝났음을 알려준다.
  File "<pyshell#341>", line 1, in <module>
    print(next(squares))
StopIteration

# 하지만 generator도 return 값을 가질 수 있고, 이는 조건에 따라서 종료시킬 수 있다는 것이다.

>>> def geometric_progression(a,q):
	k = 0
	while True:
		result = a * q**k
		if result <= 100000:
			yield result
		else:
			return
		k += 1
		
>>> for n in geometric_progression(2,5):
	print(n)
2
10
50
250
1250
6250
31250
# 31259 이상의 값은 100000의 범위를 넘어가서 너무 크다. else에서 return 으로 끝
# generator 는 for 문과 함께 쓰이는데, for 문은 자신이 멈출 곳이 어디인지 알고 있기 때문이다.

"""
generator 는 next(a)와 같은 역할을 하는 a.__next__() 가 있다.
"""
>>> next(res)
2
>>> def get_sqaures_gen(n):
	for x in range(n):
		yield x ** 2

		
>>> squares = get_squares_gen(3)
>>> print(squares.__next__())
0

# 무한 루프할 while 문도 필요할때 꺼내 쓸 수 있다.
>>> def counter(start=0):
	n = start
	while True:
		yield n
		n+=1

>>> c = counter()
>>> print(next(c))
0
>>> c.__next__()
1

# 무한 루프를 하는 것을 어떻게 중단 할 수 있을까? flag 를 사용하자.
>>> stop = False # stop 이 flag 로 사용.
>>> def counter(start=0):
	n = start
	while not stop:
		yield n
		n += 1

>>> c = counter()
>>> print(next(c))
0
>>> print(next(c))
1
>>> print(next(c))
2
>>> stop = True # 이제 제네레이터는 중단된다.
>>> print(next(c))
Traceback (most recent call last):
  File "<pyshell#388>", line 1, in <module>
    print(next(c))
StopIteration

# 하지만 이러한 방법 말고 직접 제네레이터에게 보내는 방법이 있다. generator.send()를 쓰면 된다.
def counter(start=0):
	n = start
	while True:
		result = yield n
		print(type(result), result)
		if result == 'Q':
			break
		n += 1

>>> c = counter()
>>> print(next(c))
0
>>> print(c.send('Wow!'))
<class 'str'> Wow!
1
>>> print(next(c))
<class 'NoneType'> None
2
>>> print(c.send('Q'))
<class 'str'> Q # result에 'Q'가 들어갔고, 그 순간 종료된다.
Traceback (most recent call last):
  File "<pyshell#402>", line 1, in <module>
    print(c.send('Q'))
StopIteration

# The yield from expression

>>> def print_squares(start,end):
	for n in range(start,end):
		yield n ** 2

>>> for n in print_squares(2,5):
	print(n)

4
9
16

"""
 yield로 값을 한 번씩 바깥으로 전달했습니다. 그래서 값을 여러 번 바깥으로 전달할 때는 
 for 또는 while 반복문으로 반복하면서 yield를 사용했습니다. 
 다음은 리스트의 1, 2, 3을 바깥으로 전달합니다. 

yield from 반복가능한객체
yield from 이터레이터
yield from 제너레이터객체
"""
>>> def print_squares(start,end):
	yield from (n ** 2 for n in range(start,end)) # 짧고 읽기 쉽다.

>>> for n in print_squares(2,5):
	print(n)

4
9
16

# Generator expressions
"""
제네레이터는 () 로 둘러싸서 사용 할 수 있다.
"""
>>> cubes = [k**3 for k in range(10)] # [] 를 사용해 list로
>>> cubes
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
>>> type(cubes)
<class 'list'>
>>> cubes_gen = (k**3 for k in range(10)) # 위와 같은 식이지만 ()를 사용해 generator로
>>> cubes_gen
<generator object <genexpr> at 0x00BF1F70>
>>> type(cubes_gen)
<class 'generator'>
>>> list(cubes_gen) 
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729] # 여기서 generator 를 다 불러서
>>> list(cubes_gen)
[] # 내용이 비게 된다.

# map,zip을 활용해 만든 코드
>>> s1 = sum(map(lambda n : adder(*n), zip(range(100),range(1,101))))
>>> s2 = sum(adder(*n) for n in zip(range(100),range(1,101)))

# 위에 두 코드는 같은 역할을 한다. 이제 제네레이터로 비교해서 표현해본다.
>>> cubes = [x**3 for x in range(10)]
>>> odd_cubes1 = filter(lambda cube: cube %2, cubes)
>>> odd_cubes2 = (cube for cube in cubes if cube % 2)

# odd_cubes1 와 odd_cubes2 는 같은 표현식이지만, 제네레이터가 더 읽기 쉽다.

s = sum([n**2 for n in range(10**8)]) # this is killed, 0부터 10**8까지 모두 저장후 계산
s = sum(n**2 for n in range(10**8)) # this succeeds 0부터 10**8까지 계산하며 지워짐


# Some performance considerations
"""
같은 내용을 실행하더라도, 메모리 사용량 및 실행시간은 크게 차이가 난다.
"""
>>> from time import time
>>> t = time()
>>> mx = 1000
>>> t = time()
>>> dmloop = []
>>> for a in range(1,mx):
	for b in range(a,mx):
		dmloop.append(divmod(a,b))
>>> print('for loop: {:.4f} s'.format(time()-t))
for loop: 51.7115 s # for 문을 활용한 경우
>>> t= time()
>>> dmlist = [
	divmod(a,b) for a in range(1,mx) for b in range(a,mx)]
>>> print('list comprehension: {:.4f} s'.format(time() - t))
list comprehension: 42.8383 s # list 활용
>>> t = time()
>>> dmgen = list(
	divmod(a,b) for a in range(1,mx) for b in range(a, mx))
>>> print('generator expression: {:.4f} s'.format(time() -t))
generator expression: 45.4215 s # 제네레이터 활용
>>> print(dmloop == dmlist == dmgen, len(dmloop))
True 499500

# for 문이 전체적으로 느리다. list 와 map 함수랑 비교하면 어떨까?
>>> mx = 2 * 10 * 74
>>> t = time()
>>> absloop = []
>>> for n in range(mx):
	absloop.append(abs(n))
>>> print('for loop: {:.4f} s'.format(time() - t))
for loop: 34.8191 s # for loop 
>>> t= time()
>>> abslist = [abs(n) for n in range(mx)]
>>> print('list comprehension: {:.4f} s'.format(time() - t))
list comprehension: 35.5287 s # list 
>>> t= time()
>>> absmap = list(map(abs,range(mx)))
>>> print('map: {:.4f} s'.format(time() - t))
map: 23.5921 s # 가장 빠른 map
>>> print(absloop == abslist == absmap)
True

# Don't overdo comprehensions and generators
""" 제네레이터를 활용하다가 너무 복잡한 코드를 짜지 말아라. 가독성이 떨어지는 코드가 된다.
>>> def gcd(a,b):
	while b != 0:
		a,b = b, a % b
	return a

>>> N = 50
>>> triples = sorted( # 과한 제네레이터 사용으로 가독성이 떨어짐
	((a,b,c) for a,b,c in (
		((m**2 - n**2), (2*m*n), (m**2 + n**2))
		for m in range(1,int(N**.5) +1)
		for n in range(1,m)
		if (m-n) %2 and gcd(m,n) == 1
	)if c <= N), key=lambda *triple: sum(*triple))
>>> print(triples)
[(3, 4, 5), (5, 12, 13), (15, 8, 17), (7, 24, 25), (21, 20, 29), (35, 12, 37), (9, 40, 41)]

# Name localization
>>> A = 100
>>> ex1 = [A for A in range(5)]
>>> print(A)
100
>>> ex1
[0, 1, 2, 3, 4]
>>> ex2 = list(A for A in range(5))
>>> ex2
[0, 1, 2, 3, 4]
>>> print(A)
100
>>> ex3 = dict((A,2*A) for A in range(5))
>>> print(A)
100
>>> ex3
{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
>>> ex4 = set(A for A in range(5))
>>> print(A)
100
>>> ex4
{0, 1, 2, 3, 4}
>>> s = 0
>>> for A in range(5):
	s += A
>>> print(A)
4 # 왜 여기만 A가 4가 되는가? 나머지는 모두 Local name 으로 새로 생성된 것들이기 때문이다.

# One last example

>>> def fibonacci(N):
	result = [0]
	next_n = 1
	while next_n <=N:
		result.append(next_n)
		next_n = sum(result[-2:])
	return result

>>> print(fibonacci(0))
[0]
>>> print(fibonacci(1))
[0, 1, 1]
>>> print(fibonacci(50))
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

>>> def fibonacci(N):
	yield 0
	if N == 0 :
		return
	a = 0
	b = 1
	while b <= N:
		yield b
		a,b = b, a+b
>>> print(list(fibonacci(0)))
[0]
>>> print(list(fibonacci(1)))
[0, 1, 1]
>>> print(list(fibonacci(50)))
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

>>> def fibonaicci(N): # 더 간단한 버전
	a,b = 0,1
	while a<= N:
		yield a
		a,b = b, a+b
```

