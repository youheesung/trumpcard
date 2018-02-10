from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    Play,
    Review,
    )
# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    summer_note_fields = ('content',)


admin.site.register(Review, PostAdmin)
admin.site.register(Play)

