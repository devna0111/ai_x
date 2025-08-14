from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE, # 1:1, 1:N에서는 설정하지 않으면 에러 발생. User 삭제 시 Profile도 삭제
                                )
    phone_number = models.CharField(max_length=20,
                                    verbose_name="전화번호",                                    
                                    )
    address = models.CharField(max_length=100,
                                verbose_name="주소",
                                )
    def __str__(self) :
        return "{}({}-{})".format(self.user.username,
                                self.phone_number,
                                self.address)