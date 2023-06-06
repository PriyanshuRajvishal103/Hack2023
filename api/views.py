from django.shortcuts import render
from django.http import JsonResponse

def first_api(request):
    data = {"message": "Hello, world!"}
    return JsonResponse(data)
