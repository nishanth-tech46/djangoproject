from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serialiazers import StudentSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class StudentListCreate(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetail(APIView):
    def get_object(self,pk):
        return Student.objects.get(pk=pk)

    def get(self,request,pk):
        student=self.get_object(pk)
        serializer=StudentSerializer(student)
        return Response(serializer.data)
    def put(self,request,pk):
        student=self.get_object(pk)

        serializer=StudentSerializer(student,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self,request,pk):
        student=self.get_object(pk)
        student.delete()
        return Response({
            "message": "Student deleted successfully"
                         })
    

