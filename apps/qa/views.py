from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Question,Answer

class QaMainView(TemplateView):
    template_name = "qa_page.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.filter(is_active = True)
        return context