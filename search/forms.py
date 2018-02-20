from .models import (
    Play,
    Review
    )
from django import forms
from django_summernote.widgets import SummernoteWidget


class PlayForm(forms.ModelForm):
    class Meta:
        model = Play
        exclude = ['playid', 'placeid', 'minprice', 'grade', 'rate']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'rate']
        widgets = {
            'content': SummernoteWidget(),
            'rate': forms.HiddenInput(),
          }
