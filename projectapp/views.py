from django.shortcuts import render,redirect
from .models import Basicform


# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        print(name,email,phone)
        #save data to the database
        Basicform.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address
             )

        return redirect('/')

    return render(request,"index.html")
