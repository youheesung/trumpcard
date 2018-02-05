from django  import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    )
from .models import Profile

class AuthForm(AuthenticationForm):
    error_message={
        'invaild_login': '아이디 또는 패스워드 틀림 ',
        'inactive':'탈퇴한 계정임',
    }

 ## 회원가입하는 곳
class SignupForm(UserCreationForm):
    error_message={
        'password_mismatch':'패스워드가 일치하지 않습니다.'
    }
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email is not None:
            return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

## 프로필 입력하는 곳임
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exculde = ('user', 'image')