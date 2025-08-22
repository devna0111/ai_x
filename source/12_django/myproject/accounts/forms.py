from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User
from .models import Profile
class SignupForm(UserCreationForm) :
    phone_number = forms.CharField(max_length=20,
                                label="전화번호",                                    
                                )
    address = forms.CharField(max_length=100,
                                label="주소",
                                )
    class Meta(UserCreationForm.Meta) :
        model = User
        # fields = ("username", "password1", "password2") # super().Meta.fields
        fields = UserCreationForm.Meta.fields + ("email",)
        labels = {
            "username" : "닉네임",
            "email" : "이메일",
            "password1" : "비밀번호",
            "password2" : "비밀번호 확인",
        }
    def save(self,commit=True) :
        user = super().save()
        profile = Profile(user=user,
                        phone_number=self.cleaned_data.get("phone_number"),
                        address=self.cleaned_data.get("address"),
                        )
        profile.save()
        return profile