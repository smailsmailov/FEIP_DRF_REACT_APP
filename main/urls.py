from django.urls import path
from .views import index , SignIn , SignUp , LogOut

urlpatterns = [
    path('',index,name='index'),
    path('registration/',SignUp,name='registr'),
    path('auth/', SignIn, name='auth'),
    path('logout',LogOut, name = 'logout')
]
