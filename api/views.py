from django.shortcuts import render
from django.http import JsonResponse
import json

def first_api(request):
    with open('api\json\info.json') as f:
        data = json.load(f)
    return JsonResponse(data)
