from django.db import models


# Create your models here.
# UserModel이라는 클래스를 만들기, 안에는 유저이름/비밀번호/바이오/생성날짜/업데이트날짜의 정보가 있다.
# Meta라는 클래스는 db테이블에 정보를 넣어주는 역할을 한다.
class UserModel(models.Model):
    class Meta:
        db_table = "my_user"

    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)
    bio = models.CharField(max_length=256, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)