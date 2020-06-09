# class , object and instance

 object는 개념, 소프트웨어 세계에 구현할 대상이다. 이를 구현하기 위한 설계도가 class. 이 설계도에 따라 만들어진(메모리에 올라간) 실체가 instance이다.

```python

class Quadrangle:
    width =0
    height = 0
    color = "black"
     def get_area(self):
         return self.width + self.height
```
* 파이썬 method는 항상 첫 번째 파라미터로 self 사용, 클래스의 변수들을 부를땐 self 사용

#### 클래스 변수와 인스턴스 변수
* 클래스 변수 : 클래스 정의에서 메서드 밖에 존재하는 변수
    * 해당 클래스를 사용하는 모두에게 공용으로 사용되는 변수
    * 클래스 변수는 클래스 내외부에서 "클래스명.변수명"으로 엑세스 가능
    * 또는 클래스 메소드(@classmethod)에서 "cls.변수명"으로 사용할 수 있음
  
* 인스턴스 변수 : 클래스 정의에서 메서드 안에서 사용되며, "self.변수명"처럼 사용되는 변수
    * 각 객체별로 서로 다른 값을 가짐
    * 클래스 내부에서는 self.인스턴스변수명을 사용하여 엑세스, 클래스 밖에서는 객체명.인스턴스변수명 으로 엑세스
    
    
