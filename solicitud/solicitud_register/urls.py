from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.request_form, name = 'request_insert'),
    path('<int:id>/', views.request_form, name = 'request_update'),
    path('delete/<int:id>/', views.requests_delete, name = 'request_delete'),
    path('list/', views.requests_list, name = 'request_list')
]
