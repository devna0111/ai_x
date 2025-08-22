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

from django.db.models.signals import post_save
from django.core.mail import send_mail
from myproject import settings
# 이벤트 처리 == signals 사용 (post_save) : profile.save() 성공 시 가입 인사를 메일 전송
def on_send_mail(sender, **kwargs) :
    """
    kwargs :
    {'signal': <django.db.models.signals.ModelSignal object at 0x000001D993C2B0D0>,
    'instance': <Profile: wjdwhdgur(010-1234-5678-서울)>, 
    'created': True, 
    'update_fields': None, 
    'raw': False, 
    'using': 'default'}
    """
    print("on_send_mail", kwargs)
    if kwargs['created'] : # True : 새로 생성된 경우, False : 각종 수정된 경우
        user = kwargs['instance'].user
        if not user.email : # 회원 가입 시 메일 입력 안 한 경우
            print("메일 입력하지 않은 계정으로 메일 발송 제한")
            return
        subject = f"안녕하세요, {user.username}님, 회원가입 감사합니다"
        body = f"안녕하세요, {user.username}님, 최상의 서비스를 어쩌구 저쩌구"
        bodyHtml = f"<h1>안녕하세요, {user.username}님,</h1></br><p> 최상의 서비스를 어쩌구 저쩌구</p>"
        send_mail(
            subject=subject,
            message=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )
    pass

# 연결 : on_send_mail 함수와 post_save 연결
post_save.connect(on_send_mail, sender=Profile)