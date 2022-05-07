from django.shortcuts import HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.


class TestView(TemplateView):
    template_name = 'application/page_test.html'


class AuthenticationView(TemplateView):
    template_name = 'application/login.html'