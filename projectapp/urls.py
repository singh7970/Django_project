from django.urls import path
from .import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('showall/',views.showall,name='showall'),
    path('home/',views.home,name='home'),
    path("",views.data,name='data')


]

