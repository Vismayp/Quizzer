from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'difficulty')
    list_filter = ('difficulty',)
    search_fields = ('question_text',)