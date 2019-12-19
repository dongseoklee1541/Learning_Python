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


```

