from os import stat
from urllib import request, response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from user.models import User
from user.serializers import UserSerializer, LoginSerializer

from django.core.files.storage import default_storage

from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from rest_framework.decorators import api_view
import jwt, datetime

# Create your views here.
@csrf_exempt
def user(request,id=0):
    if request.method=='GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    elif request.method=='POST':                                    #register
        users_data=JSONParser().parse(request)
        users_serializer = UserSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

@csrf_exempt 
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

@api_view(['POST'])
@csrf_exempt
def login(request):
    #return JsonResponse("Reacher Here Successfully!!" , safe=False)
    if request.method == 'POST':
        #print("at least reached destination")
        users_data=JSONParser().parse(request)
        login_serializer = LoginSerializer(data=users_data)
        if login_serializer.is_valid(): 
            temp_username = str(login_serializer['username'])
            temp_password = str(login_serializer['password'])
            username = temp_username[18:-13]
            password = temp_password[18:-13]
            print("username is ", username, "password is ", password)

            '''username = request.data('username')
            password = request.data('password')
            '''
            user = User.objects.filter(username=username).first()

            if user is None:
                raise AuthenticationFailed('User not found')
            elif password!=user.password:
                raise AuthenticationFailed('Incorrect Password')
        
            payload = {
                'username' : username,
                'exp' : datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
                'iat' : datetime.datetime.utcnow()
            }
            token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

            response = Response()

            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
                'jwt': token
            }
            return response
        
        return Response({
            'messsage' : 'Serialization Error'
        })


@api_view(['GET'])
@csrf_exempt
def userView(request):
    if request.method == 'GET':
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        print(payload['username'])
        user = User.objects.filter(username=payload['username']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

@api_view(['POST'])
@csrf_exempt
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response

@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)