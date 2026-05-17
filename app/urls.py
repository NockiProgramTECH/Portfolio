from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projet/<int:pk>/', views.project_detail, name='project_detail'),
    path('ajax/contact/create/', views.ajax_contact_create, name='ajax_contact_create'),
    path('ajax/contact/list/', views.ajax_contact_list, name='ajax_contact_list'),
]

