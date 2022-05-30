from django.urls import path
from .views import MemeberSignUp

urlpatterns = [
    path('signup/', MemeberSignUp.as_view(), name='signup')
]