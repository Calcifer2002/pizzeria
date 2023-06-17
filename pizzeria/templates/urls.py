from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('order/<int:pizza_id>/', views.order, name='order'),
    path('confirmation/<int:order_id>/', views.confirmation, name = 'confirmation') 
]

