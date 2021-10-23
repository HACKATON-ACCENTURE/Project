from django.urls import path, include
from . import views

urlpatterns = [
    path('tables', views.tables, name='tables'),
    path('', views.index, name = 'index'),
    path('KPI', views.kpi, name = 'kpi')
]