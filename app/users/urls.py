"""
URL mapping for users App APIs.
"""
from django.urls import path
from users import views

app_name = 'user'

urlpatterns = [
    path('', views.ListCreateUserView.as_view(), name='list-create'),
    path('<int:pk>/', views.DetailUserView.as_view(), name='user'),
    path('me/', views.ManageProfileView.as_view(), name='me'),
]
