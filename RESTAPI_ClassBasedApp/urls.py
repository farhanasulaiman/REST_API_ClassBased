from django.urls import path

from RESTAPI_ClassBasedApp import views

urlpatterns = [

    path("test", views.Employee1.as_view(), name="test"),
    path('emp_record/<int:id>/',views.EmployeeRecord.as_view(),name='emp_record')

]
