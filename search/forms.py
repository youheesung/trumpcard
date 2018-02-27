from .models import (
    Play,
    Review,
    )
from django import forms

import sys

from django.core import validators
from django.utils.translation import ugettext_lazy as _


class MaxValueMultiFieldValidator(validators.MaxLengthValidator):
    code = 'max_multifield_value'

    def clean(self, x):
        return len(','.join(x))


class MinChoicesValidator(validators.MinLengthValidator):
    message = _(u'You must select a minimum of  %(limit_value)d choices.')
    code = 'min_choices'


class MaxChoicesValidator(validators.MaxLengthValidator):
    message = _(u'You must select a maximum of  %(limit_value)d choices.')
    code = 'max_choices'


if sys.version_info[0] == 2:
    string = basestring  # noqa: F821
    string_type = unicode  # noqa: F821
else:
    string = str
    string_type = string


def get_max_length(choices, max_length, default=200):
    if max_length is None:
        if choices:
            return len(','.join([string_type(key) for key, label in choices]))
        else:
            return default
    return max_length


class MultiSelectFormField(forms.MultipleChoiceField):
    widget = forms.CheckboxSelectMultiple

    def __init__(self, *args, **kwargs):
        self.min_choices = kwargs.pop('min_choices', None)
        self.max_choices = kwargs.pop('max_choices', None)
        self.max_length = kwargs.pop('max_length', None)
        super(MultiSelectFormField, self).__init__(*args, **kwargs)
        self.max_length = get_max_length(self.choices, self.max_length)
        self.validators.append(MaxValueMultiFieldValidator(self.max_length))
        if self.max_choices is not None:
            self.validators.append(MaxChoicesValidator(self.max_choices))
        if self.min_choices is not None:
            self.validators.append(MinChoicesValidator(self.min_choices))


class CreatePlayForm(forms.ModelForm):
    class Meta:
        model = Play
        exclude = ['playid', 'placeid', 'minprice', 'grade', 'rate', 'genre_select', 'play_char', 'poster', 'styurl1', 'styurl2', 'styurl3', 'styurl4', 'to_my_heart', 'confirmed', 'user_upload', 'author']
        widgets = {
            'start_date' : forms.DateInput(attrs={'class':'vDateField'}),
            'end_date' : forms.DateInput()
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'rate', 'tag', 'img1', 'img2', 'img3', 'img4']
        widgets = {
            'rate': forms.HiddenInput(),
            }
