from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict, name='predict'),
    path('logout/', views.signout, name='signout'),
    path('', views.index, name='index')
]