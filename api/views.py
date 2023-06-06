from django.shortcuts import render
from django.http import JsonResponse

def first_api(request):
    data = {"message": "Hello, kids!","age":100}
    return JsonResponse(data)
