from django.urls import path
from .views import index , SignIn , SignUp , LogOut

urlpatterns = [
    path('',index,name='index'),
    path('SignUp/',SignUp,name='registr'),
    path('SignIn/', SignIn, name='auth'),
    path('Logout/',LogOut, name = 'logout')
]
