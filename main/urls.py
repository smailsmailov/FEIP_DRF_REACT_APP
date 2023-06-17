from django.urls import path
from .views import index , SignIn , SignUp , LogOut , Favorite , Buy_list_check , Category_serach , Item_to_display

urlpatterns = [
    path('',index,name='index'),
    path('signUp',SignUp,name='signup'),
    path('signIn', SignIn, name='signin'),
    path('logout',LogOut, name = 'logout'),
    path('favorite',Favorite,name='favorite'),
    path('buy_list',Buy_list_check,name='buy_list'),
    path('search',Category_serach,name='search'),
    path('item/<int:id>/',Item_to_display,name='item'),
]

