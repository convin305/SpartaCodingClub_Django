from django.contrib import admin
# 어드민 툴 사용
from .models import UserModel
# 우리가 생성한 모델 사용

# Register your models here.
admin.site.register(UserModel) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다