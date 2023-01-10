from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_coins, name='coins'),
    path('<int:coins_id>/', views.coins_detail, name='coins_detail'),
    path('add/', views.add_coins, name='add_coins'),
    path('edit/<int:coins_id>/', views.edit_coins, name='edit_coins'),
    path('delete/<int:coins_id>/', views.delete_coins, name='delete_coins'),
]
