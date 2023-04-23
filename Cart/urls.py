from django.urls import path
from .import views

app_name = 'Cart'

urlpatterns = [
    path('start_order/',views.start_order, name='start_order'),    
    path('add_to_cart/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('remove_from_cart/<int:product_id>',views.remove_from_cart,name='remove_from_cart'),
    path('change_quantity/<str:product_id>',views.change_quantity,name='change_quantity'),
    path('cart/', views.cart_view,name='cart_view'),       
]