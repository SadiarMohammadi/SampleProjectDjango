from django.urls import path

from employee import views

urlpatterns = [
    path('', views.show),
    path('emp/', views.emp, name='emp'),

]
