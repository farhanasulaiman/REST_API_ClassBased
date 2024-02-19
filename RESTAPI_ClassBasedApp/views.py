from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from RESTAPI_ClassBasedApp.models import Employee
from RESTAPI_ClassBasedApp.serializer import EmployeeSerializer


# Create your views here.


class Employee1(APIView):

    def get(self, request):
        emp_data = Employee.objects.all()
        serializer = EmployeeSerializer(emp_data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeRecord(APIView):
    def get_id(self, id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            # except Employee.AttributeError:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        emp = self.get_id(id)
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data)

    def put(self, request, id):
        emp = self.get_id(id)
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        emp = self.get_id(id)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
