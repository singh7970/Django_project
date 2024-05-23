from django.urls import path
from .import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('showall/',views.showall,name='showall'),
    path('home/',views.home,name='home'),
    path("data/",views.data,name='data'),
    path('delete/<int:contact_id>/', views.delete, name='delete'),
    path('delete_data/<int:data_id>/', views.delete_data, name='delete_data'),
    path("",views.insta,name='insta'),




    

    



]

