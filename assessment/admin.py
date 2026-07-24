from django.contrib import admin
from .models import Principle, Question, Choice, Assessment, Answer


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "principle", "order")
    inlines = [ChoiceInline]


admin.site.register(Principle)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Assessment)
admin.site.register(Answer)
