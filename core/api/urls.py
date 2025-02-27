from django.urls import path

from core.api.confirm_email import confirm_email
from core.api.forgot_password import forgot_password
from core.api.reset_password import reset_password
from core.api.login_view import api_login
from core.api.register_view import register
from core.api.dummy_game_list import dummy_game_list

urlpatterns = [
    path('core/dummy-data/', dummy_game_list, name='dummy_game_list'),
    path('core/login/', api_login, name='api_login'),
    path('core/register/', register, name='register'),
    path('core/confirm-email/<uidb64>/<token>/', confirm_email, name='confirm_email'),
    path('core/forgot-password/', forgot_password, name='forgot_password'),
    path('core/reset-password/<uidb64>/<token>/', reset_password, name='reset_password'),
]