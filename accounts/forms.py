
from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    )
from .models import (
    Profile,
    )
# from .models import Profile


class AuthForm(AuthenticationForm):
    error_message= {
        'invaild_login': '아이디 또는 패스워드 틀림 ',
        'inactive': '탈퇴한 계정임',
    }

# 회원가입하는 곳
class SignupForm(UserCreationForm):
    error_message = {
        'password_mismatch': '패스워드가 일치하지 않습니다.'
    }
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email is not None:
            return email
            # email 다시 유저 대상으로 customize 하기

    def save(self, commit=True): # commit = True
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# 프로필 수정하는 곳임
class SignupProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'image', 'group_image', 'genre_select', 'play_char')


# 프로 필 form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

# 극단 회원가입

class GroupProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'birth_date', 'liebe_t', 'liebe_a', 'recommand_t', 'image', 'genre_select', 'play_char')

# 프로필 수정하는 공간 만들기
