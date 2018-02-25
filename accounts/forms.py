
from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    )
from .models import (
    Profile,
    )
# from .models import Profile


# -*- coding: utf-8 -*-
# Copyright (c) 2012 by Pablo Martín <goinnn@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this programe.  If not, see <http://www.gnu.org/licenses/>.


class AuthForm(AuthenticationForm):
    error_message = {
        'invaild_login': '아이디 또는 패스워드 틀림 ',
        'inactive': '탈퇴한 계정임',
    }


# 회원가입하는 곳
class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

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
        exclude = ('user', 'image', 'group_image', 'genre_select', 'play_char', 'follow', 'liebe_t', 'liebe_a', 'recommand_t')


# 프로 필 form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

# 극단 회원가입


class GroupProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'birth_date', 'recommand_t', 'image', 'genre_select', 'play_char', 'follow', 'liebe_t', 'liebe_a', )


# 프로필 수정하는 공간 만들기
