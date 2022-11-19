from django.urls import path
from .import views as v
urlpatterns = [
    path('register_user', v.registration_request),
    path('home_page', v.homepage),
    path('login_user', v.login_user),
    path('logout_user', v.logout_user)
]
