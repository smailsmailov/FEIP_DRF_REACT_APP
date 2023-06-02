from django.urls import path
from .views import index , SignIn , SignUp , LogOut , Favorite

urlpatterns = [
    path('',index,name='index'),
    path('signUp',SignUp,name='signup'),
    path('signIn', SignIn, name='signin'),
    path('logout',LogOut, name = 'logout'),
    path('favorite',Favorite,name='favorite')
]
