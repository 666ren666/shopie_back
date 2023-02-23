
from django.urls import path
from . import views 
from product.views import delete_product, update_product, product
from product.views import delete_cart_item, update_cart_item, cart_item
from product.views import add_to_cart



urlpatterns = [
    path('products/', views.products),
    path('product/<int:pk>', product, name='product'),
    path('product/<int:pk>/delete/', delete_product, name='delete_product'),
    path('product/<int:pk>/update/', update_product, name='update_product'),

    path('cart_items/', views.cart_items),
    path('cart_item/<int:pk>', cart_item, name='cart_item'),
    # path('cart_item/<int:pk>/delete/', delete_cart_item, name='delete_cart_item'),
        path('api/delete_cart_item/<int:pk>/', delete_cart_item, name='delete_cart_item'),

    path('cart_item/<int:pk>/update/', update_cart_item, name='update_cart_item'),

    path('api/add_to_cart/', add_to_cart, name='add_to_cart'),


]