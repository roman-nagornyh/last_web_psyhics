from django.urls import path, include
from .views import AuthenticationView

urlpatterns = [
    path('', AuthenticationView.as_view(), name='login')

]