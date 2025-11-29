from django.urls import path
from Placements import views

urlpatterns = [
    path('', views.Placements, name='placements'),
    path('company/<int:c_id>/', views.companies_detail, name='companies_detail'),
    # path('forms/', views.forms, name='forms'),
]