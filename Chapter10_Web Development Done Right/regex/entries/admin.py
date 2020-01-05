from django.contrib import admin
from .models import Entry

# Register your models here.
@admin.register(Entry)
#admin.register를 사용하면 앱을 옮기거나 이름을 바꿀 수 있다.
#데코레이션은 장고에게 엔트리 모델을 관리 패널에 표시하도록 하고
#EntryAdmin 클래스에 넣은 것은 장고에게 이 모델을 처리하는 방법을 알려준다
class EntryAdmin(admin.ModelAdmin):
	fieldsets = [
	('Regular Expression',
	{'fields' : ['pattern', 'test_string']}),
	('Other Information',
	{'fields': ['user', 'date_added']}),
	]
#목록 페이지에 결과를 표시
	list_display = ('pattern', 'test_string', 'user')
	list_filter = ['user']
	search_fields = ['test_string']
	