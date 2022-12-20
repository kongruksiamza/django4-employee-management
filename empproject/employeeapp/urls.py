from django.urls import path
from employeeapp import views

urlpatterns = [
    path('', views.index),
    path('create',views.create),
    path('delete/<emp_id>',views.delete,name="delete"),
    path('edit/<emp_id>',views.edit,name="edit")
]