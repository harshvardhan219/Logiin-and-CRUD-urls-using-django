from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.student_form, name="student_insert"), #get and post operation
    path('<int:id>/', views.student_form, name="student_update"),#get and post request for update operation
    path('delete/<int:id>',views.student_delete, name="student_delete"),
    path('list/',views.student_list, name="student_list"),#get required to retreive and display all records
]
