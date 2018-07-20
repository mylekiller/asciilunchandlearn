from django.contrib import admin
from .models import Question, Choice, Team

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Team)