from django.urls import path
from accounts.views import *

urlpatterns = [
    path('login/', login_user_api, name='login_api_page'),
    path('register/', register_user_api, name='register_api_page'),
    path('user/', get_user_api, name='get_user_api_page'),

]