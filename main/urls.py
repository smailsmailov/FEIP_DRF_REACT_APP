from django.urls import path
from .views import index , SignIn , SignUp , LogOut , Favorite , Buy_list_check

urlpatterns = [
    path('',index,name='index'),
    path('signUp',SignUp,name='signup'),
    path('signIn', SignIn, name='signin'),
    path('logout',LogOut, name = 'logout'),
    path('favorite',Favorite,name='favorite'),
    path('buy_list',Buy_list_check,name='buy_list')
]

