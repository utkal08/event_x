from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/',views.about,name='about'),
    path('contact_us/', views.ContactUsView.as_view(), name='contact'),
]
