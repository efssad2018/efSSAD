from django.urls import path
from . import views


urlpatterns = [
    #re_path(r'^$/', views.login, name='login'),
    #path('', views.login, name=''),
    path('mcmain/', views.mcmain, name='mcmain'),
    path('scmission/', views.scmission, name='scmission'),

]