from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ZodioscopeHomeView(TemplateView):
    template_name = 'zodioscope/home.html'

class DailyZodioscopeView(TemplateView):
    template_name = 'zodioscope/daily.html'