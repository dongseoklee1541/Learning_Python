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

