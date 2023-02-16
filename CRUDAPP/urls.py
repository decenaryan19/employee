from django.urls import path
from . import views

urlpatterns = [
    

    # '' inmdicates as the home page or landing page 
    path('', views.insert_emp, name='insert-emp'),
    path('show/', views.show_emp, name='show-emp'),
    path('edit/<int:pk>', views.edit_emp, name='edit-emp'),
    path('remove/<int:pk>', views.remove_emp, name='remove-emp'),
     path('', views.home),
    path("simple_function", views.simple_function),
   ]