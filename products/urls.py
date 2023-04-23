from django.urls import path
from .import views

app_name = 'products'

urlpatterns = [

    path('',views.product_list,name='products'),
    path('<str:id>/',views.product_detail, name='product_detail'),
           
]