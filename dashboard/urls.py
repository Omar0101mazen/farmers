from django.urls import path
from .import views

app_name = 'dashboard'

urlpatterns = [
      
    path('',views.dashboard,name='dashboard'), 
    path('delete/<int:id>',views.delete,name='delete'),     
]
# {% url 'delete' product.id %}delete