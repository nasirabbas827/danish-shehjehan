from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.custom_register, name='register'), 
    path('login/', views.custom_login, name='login'),            
    path('logout/', views.custom_logout, name='logout'),         
    path('update_profile/', views.update_profile, name='update_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('election/<int:election_id>/', views.election_detail, name='election_detail'),
    path('vote/<int:election_id>/<int:candidate_id>/', views.vote, name='vote'),
    path('election_winners/', views.election_winners, name='election_winners'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
