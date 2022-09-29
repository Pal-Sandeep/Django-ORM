from django.urls import path
from django.contrib import admin
from .  import views
urlpatterns = [
    path('',views.index,name='index'),
    path('create',views.create_view,name='create_view'),
    path('<id>/delete', views.delete_Emp,name='delete_Emp'),
    path('update/<int:pk>',views.updateEmp,name='updateEmp'),
]