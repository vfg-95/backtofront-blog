from django.urls import path
from . import views
# from .views import MemberSignUp


urlpatterns = [
    path('login/', views.UserLogin, name='userlogin'),
    # path('signup/', MemeberSignUp.as_view(), name='signup'),
]