from django.urls import path

from mybackend.urls import urlpatterns
from .views import RegisterView
urlpatterns=[
    path('register/', RegisterView.as_view()),
   # path('login/', loginview.as_view()),
    #path('logout/', logoutview.as_view()),
    #path('user/', UserView.as_view()),

]