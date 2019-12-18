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

