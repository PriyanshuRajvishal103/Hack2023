from django.shortcuts import render
from django.http import JsonResponse

def first_api(request):
    data = {"message": "This message has been routed from api"}
    return JsonResponse(data)
