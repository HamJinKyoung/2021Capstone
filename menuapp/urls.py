from django.urls import path
from menuapp import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('optionmenu/<int:pk>', views.optionmenu, name='optionmenu'),
    path('checkmenu/', views.checkmenu, name='checkmenu'),
    path('pay/', views.pay, name='pay'),
    path('pay/success/', views.success, name='success'),
    path('checkmenu/delete_basket/<int:pk>', views.delete_basket, name='delete_basket'),
]
