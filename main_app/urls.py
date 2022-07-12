from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shrooms/', views.shrooms_index, name='index'),
    path('shrooms/<int:shroom_id>/', views.shrooms_detail, name='detail'),
    path('shrooms/create/', views.ShroomCreate.as_view(), name='shrooms_create'),
    path('shrooms/<int:pk>/update/', views.ShroomUpdate.as_view(), name='shrooms_update'),
    path('shrooms/<int:pk>/delete/', views.ShroomDelete.as_view(), name='shrooms_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('plants/seasons/', views.seasons, name='seasons'),
    path('plants/seasons/spring/', views.spring, name='spring'),
    path('plants/seasons/summer/', views.summer, name='summer'),
    path('plants/seasons/winter/', views.winter, name='winter'),
    path('plants/seasons/fall/', views.fall, name='fall'),



]