# importing depecdencies
from django.shortcuts import render
from rest_framework import viewsets

# importing models
from .models import Information

# importing forms
from .forms import InformationForm

# importing serializers
from .serializers import InformationSerializer
from django.http import JsonResponse

class InformationViewset(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer


def home(request):
    dict = {"age": 20,}
    return render(request, "home.html",dict)

def first_api(request):
    data = {"message": "Hey there, this is rendered as api!"}
    return JsonResponse(data)

def sign(request):
    return render(request, "forms.html")


def info(request):
    if request.method == 'POST':
        form = InformationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "forms.html")
