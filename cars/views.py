from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
# Create your views here.

@api_view()
def hello_world(request):
    return Response({"message": "Hello, Suraj "})

@api_view(['GET'])
def carview(request):
    crs= Car.objects.all().values()
    return Response({"car collections": crs})

@api_view(['GET'])
def filterview(request):
    crs= Car.objects.filter(color="BLACK").values()
    return Response({"BLACK COLOR CARS": crs})

@api_view(['DELETE'])
def deleteview(request):
    Car.objects.filter(brandname="FORD").delete()
    return Response({"Deleted":" you deleted successfully"})

@api_view(['POST'])
def createview(request):
    b_name=request.POST.get("brandname")
    m_name=request.POST.get("model")
    c_color=request.POST.get("color")
    c_milage=request.POST.get("milage")
    c_rent=request.POST.get("rent")
    Car.objects.create(brandname=b_name, modelname=m_name, color=c_color, 
    milage=c_milage, rentperday=c_rent)
    return Response({"insert":" you inserted successfully"})



