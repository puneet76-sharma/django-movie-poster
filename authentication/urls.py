from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', sign_up, name='signup'),
    path('login/', user_login, name='login'),
    path('profile/', user_profile, name='profile'),
    path('logout/', user_logout, name='logout'),
    path('user-details/<int:id>/', user_details, name='user_details'),




]