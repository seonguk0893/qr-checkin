from django.urls import path
from . import views


urlpatterns = [
    path("", views.login_view, name="login"),  # 로그인 페이지
    path('home/', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('logout', views.logout_view, name='logout'),

]
