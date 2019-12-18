# CH.2 Iterating and Making Decisions

프로그램의 흐름을 통제하기 위해선 conditional programming(branching, 분기문) 과 looping(반복문)이 있다.

## Conditional programming

조건문은 여러 부분에서 사용되고 대표적으로 'if' 문이 있다.

```python
late = True
if late: # if 안의 조건이 True 일때 작동
 print('I need to call my manager!')
```

### A specialized else: elif

조건문이 아닐때 바로 또 다른 조건을 걸고 싶다면 'elif'문을 사요하면 된다.

예를 들어 수입에 따라 다른 세율을 부과하고 싶다면 말이다.

```python
income = 15000
if income < 10000:
 tax_coefficient = 0.0 #1
elif income < 30000:
 tax_coefficient = 0.2 #2
elif income < 100000:
 tax_coefficient = 0.35 #3
else:
 tax_coefficient = 0.45 #4
print('I will pay:', income * tax_coefficient, 'in taxes')
```

### The ternary operator

if 조건문을 더 간단하게 사용하는 방법이 있다.

조건부 표현식 : name = something if condition else something-else.

```python
order_total = 247

if order_total > 100:
  discount = 25
else:
  discount = 0
print(order_total,discount)

# ternary operator
discount = 25 if order_total > 100 else 0 # 조건문이 True 라면 왼쪽에 있는 값인 25를 
                                          # 아니면 else 뒤의 0을 사용
print(order_total, discount)
```

## Looping

반복문에는 for 와 while이 있다.

### The for loop

for문은 순차적으로 따라서 반복한다.

```python

for number in [0,1,2,3,4]:
  print(number)
  
for number in range(5): # range 함수를 활용
  print(number)
```

### Iterating over a sequence

```python
surnames = ['Rivest', 'Shamir', 'Adleman']
>>> for position in range(len(surnames)): # position 에 숫자를 넣고, surnames 에는 인덱스 번호로
	print(position, surnames[position])

0 Rivest
1 Shamir
2 Adleman
```

* enumerate(args) : 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능을 가진다. 
이 함수는 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받아
인덱스 값을 포함하는 enumerate 객체를 리턴한다.

```python
surnames = ['Rivest', 'Shamir', 'Adleman']
for position, surname in enumerate(surnames): # enumerate에 list가 들어와 있어, 
                                              # 순서와 리스트의 값을 넣어준다.
	print(position,surname)
  
0 Rivest
1 Shamir
2 Adleman
```

하지만 좀 더 파이썬 답게 코드를 줄여보자. 앞에서 배운 zip을 활용하면 된다.

```python
people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
nationalities = ['Belgium', 'Spain', 'England', 'Bangladesh']
for person, age, nationality in zip(people, ages, nationalities):
 print(person, age, nationality) # zip을 활용해 더 효율적으로 반복할 수 있다.

Jonas 25 Belgium
Julio 30 Spain
Mike 31 England
Mez 39 Bangladesh
```

투플로 묶어서 반환하는 방법도 있다.

```python
people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
nationalities = ['Belgium', 'Spain', 'England', 'Bangladesh']
for data in zip(people, ages, nationalities): # data는 3개의 값을 가진 투플이 되고
 person, age, nationality = data # 각각 person, age, nationality에 들어간다.
 print(person, age, nationality)
```

### The while loop

일정한 크기의 조건이 필요하다면 for 문을 사용하면 되지만, 무한하거나 특정 시점에서 반복을 종료 하고 싶다면 while
문을 사용하면 된다. 

* divmod(a,b) : 2개의 숫자를 입력으로 받고 a를 b로 나눈뒤 몫과 나머지를 투플로 반환한다.

```python
>>> n = 39
>>> remainders = []
>>> while n > 0:
	n,remainder = divmod(n,2) # 39를 2로 나누고 몫과 나머지를 반환해준다.
	remainders.append(remainder)

	
>>> remainders = remainders[::-1]
>>> print(remainders)
[1, 0, 0, 1, 1, 1]
```

* continue : 밑에 코드는 무시하고 while의 시작으로 돌아가 실행한다.
* break : 반복문을 종료한다.

### EX1. a prime generator(소수 생성기)

```python
primes = [] # 소수를 받을 녀석
upto = 100
for n in range(2,upto+1):
	is_prime = True
	for divisor in range(2,n):
		if n % divisor == 0:
			is_prime = False
			break
	if is_prime:
		primes.append(n)
print(primes)
```

```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

flag 역할을 하는 is_prime을 제거하면 더 깔끔하다.

```python
primes = []
upto = 100
for n in range(n, upto + 1):
	for divisor in range(2,n):
		if n % divisor == 0:
			break # break 문으로 나가서 처음으로 돌아가거나
	else: # 여기서 받아준다.
		primes.append(n)
print(primes)
```

### EX2. applying discounts

고객들이 갖고 있는 쿠폰에 따라 할인율을 다르게 지정하는 프로그램을 만들어 보자.

```python
customers = [
 dict(id=1, total=200, coupon_code='F20'), # F20: fixed, £20
 dict(id=2, total=150, coupon_code='P30'), # P30: percent, 30%
 dict(id=3, total=100, coupon_code='P50'), # P50: percent, 50%
 dict(id=4, total=110, coupon_code='F15'), # F15: fixed, £15
]
 
for customer in customers:
	code = customer['coupon_code']
	if code == 'F20': 
		customer['discount'] = 20.0
	elif code == 'F15':
		customer['discount'] = 15.0
	elif code == 'P30':
		customer['discount'] = customer['total'] * 0.3
	elif code == 'P50':
		customer['discount'] = customer['total'] * 0.5
	else:
		customer['discount'] = 0.0
 
for customer in customers:
	print(customer['id'], customer['total'], customer['discount'])
```

```
1 200 20.0
2 150 45.0
3 100 50.0
4 110 15.0
```

위와 같은 코드는 한눈에 보기가 어렵다. 사전형을 사용해서 더 보기 쉽게 만들어보자.

```python
customers = [
 dict(id=1, total=200, coupon_code='F20'), # F20: fixed, £20
 dict(id=2, total=150, coupon_code='P30'), # P30: percent, 30%
 dict(id=3, total=100, coupon_code='P50'), # P50: percent, 50%
 dict(id=4, total=110, coupon_code='F15'), # F15: fixed, £15
]
 
discounts = {
 'F20': (0.0, 20.0), # each value is (percent, fixed)
 'P30': (0.3, 0.0),
 'P50': (0.5, 0.0),
 'F15': (0.0, 15.0),
}
 
for customer in customers:
	code = customer['coupon_code']
	percent, fixed = discounts.get(code, (0.0, 0.0)) # .get()기존의 code가 없으면 (0.0,0.0)을 							   # 넣어라
	customer['discount'] = percent * customer['total'] + fixed
 
for customer in customers:
	print(customer['id'], customer['total'], customer['discount'])
```

코드는 2줄 더 늘었지만, 가독성이 더 높아졌다. 기존의 조건문(if)의 길이가 for 문을 통해서 많이 줄어 들었고else로 값이 없을때를 대비한 코드를 dict.get(key,default)로 해결했다.

## A quick peek at the itertools module

Python 에서 제공하는 자신만의 반복자를 만드는 모듈이다. 

### Infinite iterators

Infinite iterators은 for문을 while 문처럼 무한루프하게 만들 수 있다.

```python
from itertools import count
for n in count(5, 3): # count(a,b) : a부터 b만큼 무한히 증가시키기
	if n > 20:
		break
	print(n,end=',')
```

### Iterators terminating on the shortest input sequence

compress('ABC',(1,0,1))는 'A', 'C'를 반환해 줄 것이다. 왜냐하면 A,C는 1과 만나기 때문이다.

이를 활용하면 더 빠르고 좋게 요소들을 선택하여 뽑을 수 있다.

```python
from itertools import compress
data = range(10)
even_selector = [1,0] * 10
odd_selector = [0,1] * 10
 
even_numbers = list(compress(data,even_selector)) # 홀수 숫자의 인덱스만 , list로 받아야 볼 수있다
odd_numbers = list(compress(data,odd_selector)) # 짝수 숫자의 인덱스만

print(odd_selector)
print(list(data))
print(even_numbers)
print(odd_numbers)
```

```
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 2, 4, 6, 8]
[1, 3, 5, 7, 9]
```

### Combinatoric generators

조합생성기는 파이썬에서 permutations(순열)을 할 수 있게 만든다.

```python
from itertools import permutations
print(list(permutations('ABC')))
```
```
[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
```

