from django.urls import path
from . import views

app_name = '_users'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.LaunchView.as_view(), name='index'), # 'launch/<int:pk>/'
    path('login.index/', views.login_index, name='login-index'),
    path('users.login/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('chgpwd.index/', views.chg_pwd, name='chgpwd-index'),
    # path('change.pass/', views.change_password, name='change-password'),
]
