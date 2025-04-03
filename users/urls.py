
from django.urls import path
from django.urls import path, include
from .views import RegisterView, LoginView
urlpatterns=[
    path('register/', RegisterView.as_view(), name='register'),
   path('login/', LoginView.as_view() , name='login'),
  
    # path('logout/', LogoutView.as_view(), name='logout'),
    #path('logout/', logoutview.as_view()),
    #path('user/', UserView.as_view()),

]