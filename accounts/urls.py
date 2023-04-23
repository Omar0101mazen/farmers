from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    
    path('signup/',views.signup, name='signup'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit',views.profile_edit, name='profile_edit'),
    path('profile_user/',views.profile_user,name='profile_user'),
    path('profile_user/edit',views.profile_edit_user, name='edit_prodile_user'),
    
]