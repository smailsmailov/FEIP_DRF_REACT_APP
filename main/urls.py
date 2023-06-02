from django.urls import path
from .views import index , SignIn , SignUp , LogOut

urlpatterns = [
    path('',index,name='index'),
    path('signUp',SignUp,name='signup'),
    path('signIn', SignIn, name='signin'),
    path('logout',LogOut, name = 'logout')
]
