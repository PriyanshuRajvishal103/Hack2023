# importing depecdencies
from django.shortcuts import render
from rest_framework import viewsets

# importing models
from .models import Information

# importing forms
from .forms import InformationForm

# importing serializers
from .serializers import InformationSerializer


class InformationViewset(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer


def home(request):
    return render(request, "home.html")


def sign(request):
    return render(request, "forms.html")


def info(request):
    if request.method == 'POST':
        form = InformationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "forms.html")
