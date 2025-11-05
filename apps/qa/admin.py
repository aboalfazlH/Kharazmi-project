from django.contrib import admin
from .models import Question,Answer



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title','is_pin','is_active','is_verify','write_date','update_date',)
    list_filter = ('is_active','is_verify','is_pin','write_date','update_date',)
    search_fields = ('title','description')
    list_editable = ('is_pin','is_active','is_verify',)
    list_per_page = 25
    date_hierarchy = 'write_date'

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('title','is_best','is_active','is_true','write_date','update_date',)
    list_filter = ('is_active','is_true','is_best','write_date','update_date',)
    search_fields = ('title','description')
    list_editable = ('is_best','is_active','is_true')
    list_per_page = 25
    date_hierarchy = 'write_date'