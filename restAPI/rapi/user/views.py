from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from user.models import User
from user.serializers import UserSerializer

from django.core.files.storage import default_storage

from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from rest_framework.decorators import api_view

# Create your views here.
@csrf_exempt
def user(request,id=0):
    if request.method=='GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    elif request.method=='POST':
        users_data=JSONParser().parse(request)
        users_serializer = UserSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
def user_detail(request, pk):
   # find tutorial by pk (id)
    try: 
        user = User.objects.get(pk=pk) 
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        users_serializer = UserSerializer(user) 
        return JsonResponse(users_serializer.data) 

    elif request.method == 'PUT': 
        user_data = JSONParser().parse(request) 
        users_serializer = UserSerializer(user, data=user_data) 
        if users_serializer.is_valid(): 
            users_serializer.save() 
            return JsonResponse(users_serializer.data) 
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE': 
        user.delete() 
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

def login(request, val):

@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)