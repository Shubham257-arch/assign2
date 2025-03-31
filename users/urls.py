
from django.urls import path
from django.urls import path, include
from mybackend.urls import urlpatterns
from .views import RegisterView, LoginView
urlpatterns=[
    path('register/', RegisterView.as_view(), name='register'),
   path('login/', LoginView.as_view() , name='login'),
    #path('logout/', logoutview.as_view()),
    #path('user/', UserView.as_view()),

]