from django.urls import path
from .views import index , SignIn , SignUp , LogOut , Favorite , Buy_list_check , Category_serach , Item_to_display , Buy_check, Info


urlpatterns = [
    path('',index,name='index'),
    path('signUp',SignUp,name='signup'),
    path('signIn', SignIn, name='signin'),
    path('logout',LogOut, name = 'logout'),
    path('favorite',Favorite,name='favorite'),
    path('buy_list',Buy_list_check,name='buy_list'),
    path('search',Category_serach,name='search'),
    # path('search/<str:type_of_search>',Category_serach,name='search_with_p'),
    path('item/<int:id>/',Item_to_display,name='item'),
    path('buy_check',Buy_check,name='buy_check'),
    path('check_sms', Buy_check, name='check_sms'),
    path('info',Info,name='info')
]
