from django.db import models # base class of Entry model
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
""" 
primary key(기본키) : 테이블 내 동일한 레코드가 입력되는 경우 이를 구분해 줄
수 있는 식별자를 만들어 사용하는 데 이것이 기본키이다. 기본키를 정하지 않으면, 장고에서 추가해준다. 

ForeignKey(외래키) 테이블의 한 필드가 다른 테이블의 기본키 필드를 참조 할 때
이를 외래키라고 한다. 외래키를 통해 두 테이블을 연결하고 관계성을 가지게 할 수 있다.
CharField : 문자열 필드
DateTimeField : 기본값이 표준 시간대로 설정 되어 있는 필드 
메타 클래스는 장고에 의해 모델에 대한 모든 종류의 추가 정보를 제공하기 위해 사용된다. 
"""
class Entry(models.Model): # base class models.Model

	user = models.ForeignKey(User,on_delete=models.CASCADE)
	pattern = models.CharField(max_length=255)
	test_string = models.CharField(max_length=255)
    
	date_added = models.DateTimeField(default=timezone.now)
	
	class Meta:
		verbose_name_plural = 'entries'
