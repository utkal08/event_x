from django.urls import path
from users import views


urlpatterns = [
    path('signup', views.SignUpView.as_view(), name='sign_up'),
    path('',views.login, name='login'),
]
