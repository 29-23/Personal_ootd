from django.urls import path
from . import views

urlpatterns = [
    path('', views.imageupload),
    path('/fashion/test/', views.FashionTest.as_view())
]
