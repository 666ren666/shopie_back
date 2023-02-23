
from django.urls import path
from . import views
from .views import create_new_shopper
from .views import login_shopper, logout_shopper


urlpatterns = [
    path('api/new_shopper/', create_new_shopper, name='create_new_shopper'),
    path('api/login_shopper/', login_shopper, name='login_shopper'),
    path('api/logout_shopper/', logout_shopper, name='logout_shopper'),
    path('shoppers/', views.shoppers),
]
