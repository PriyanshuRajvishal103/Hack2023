from django.contrib import admin
from myapp import views
# from api import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import InformationViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Info',InformationViewset)

urlpatterns = [
    path('admin',admin.site.urls),
    path('my-api', views.first_api),
    path('',views.home),
    path('sign_in',views.sign),  
    path('info',views.info),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)