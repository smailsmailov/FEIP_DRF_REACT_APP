from django.urls import path
from .views import index , login , registration

urlpatterns = [
    path('',index,name='index'),
    path('registration/',registration,name='registr'),
    path('auth/', login, name='auth'),
]
