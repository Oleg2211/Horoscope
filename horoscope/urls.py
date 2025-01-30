from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:day>/<int:month>', views.get_sign_by_date),
    path('type/', views.type),
    path('type/<element>/', views.get_element, name='element-name'),
    path('<int:sign_zodiac>/', views.get_info_abaut_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_abaut_sign_zodiac, name='horoscope-name'),
]
