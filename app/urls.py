from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/contact/create/', views.ajax_contact_create, name='ajax_contact_create'),
    path('ajax/contact/list/', views.ajax_contact_list, name='ajax_contact_list'),
]

