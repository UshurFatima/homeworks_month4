from django.urls import path
from . import views

app_name = 'employees'
urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.AuthLoginView.as_view(), name='login'),
    path('logout/', views.AuthLogoutView.as_view(), name='logout'),
    path('employee_list/', views.EmployeeListView.as_view(), name='employee_list'),
]