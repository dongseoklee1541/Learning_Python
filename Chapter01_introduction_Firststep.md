## 파이썬 가상환경

파이썬에서 제공하는 가상환경은, venv, virtualenv, conda 등이 존재한다.

### virtualenv

**powershall 로 실행해야 가상환경이 실행된다. 다른 방법이 없을까?**

#### windows 기준 실행

* pip install virtualenv : pip 명령어로 모듈 설치

* virtualenv 가상환경명 : virtualenv 로 가상환경을 생성한다.

* 가상환경명/Scripts/activate : windows 가상환경 구동 방법

```
Using base prefix 'c:\\users\\vuno\\appdata\\local\\programs\\python\\python37-32'
New python executable in C:\Users\vuno\srv\learing.python\python\mypy\Scripts\python.exe
Installing setuptools, pip, wheel...
가상환경명 : mypy
```

cf. source 가상환경명/bin/activate : mac 또는 리눅스에서 가상환경 구동 방법

* 가상환경이 구동되면 터미널 창의 프롬프트가 아래와 같이 변경됨

* python -m idlelib : 파이썬 가상환경에서 ldle 기동 방법

**(가상환경명) $**

* deactivate : 가상환경을 빠져나오는 명령어

----
## Running Python Scripts

cf. 스크립트 언어 ? 스크립트 언어(scripting language)란 응용 소프트웨어를 제어하는 컴퓨터 프로그래밍 언어를 가리킨다. 스크립트 프로그래밍 언어라고도 한다.

## How is Python code organize

파이썬 코드는 모듈과 패키지로 이루어져있다. 이렇게 구별한 이유는 하나의 모듈에 수백라인의 코드를 몽땅 집어넣는것은 비효율적이기 때문이다.

* 모듈 : 코드가 저장되어 있는 .py 파일 

* 패키지 : 모듈(.py)의 묶음
  * __ init __ .py : 같은 디렉토리에 있는 .py 파일들이 하나의 패키지로 이루어져 있다는걸을 알려주는 모듈


## Python's execution model

### Names and namespaces

* Name ? code 안에 존재하는 data에 불러오기 위한 것

* Namespace ? name에서 object로 매핑되는 것 ex) 기본 제공되는 이름들, 모듈의 전역 이름, 함수의 로컬 이름 등

```python
# library라는 namespace로 부터 시작해, "."를 통해서 namespace 안으로 들어가게 되어 끝내 name인 book을 찾는다.
from library.second_floor.section_x.row_three import book
```

* Scopes ? namespace에 접근할 수 있는 범위를 뜻한다.
  * local scope : local variable/(지역변수)에 접근 할 수 있는 scope
  * enclosing scope : enclosing function에 속한 space에 접근 할 수 있는 것들, local name 도 아니고, global name도 아니다.
  * global scope : global name에 접근할 수 있다
  * built-in scope : built-in name들을 포함하는 scope이다. 파이썬에 기본적으로 설정되있는 함수들의 집합들을 가져올 수 있다. 
  ex) print, all, abs 등..
  
파이썬에서는 name 을 찾을때, current namespace에서 찾는다. name을 찾을 수 없을때, 파이썬은 encloseing scope, built-in scope 까지 찾아본다.
만약 name을 찾지 못한다면, 파이썬은 **NameError exception** 을 일으킨다. 일반적으로 name이 정의되어있지 않을때 발생한다.


