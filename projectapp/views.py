from django.shortcuts import render,redirect
from .models import Basicform,DATA


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


def showall(request):
    show=Basicform.objects.all()
    data=DATA.objects.all()
    Synt={"show":show,"data":data}
    return render(request,"showall.html",Synt)

def home(request):
    return render(request,'home.html')


def data(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        address=request.POST.get('address')
        print(password)
        DATA.objects.create(
            name=name,
            phone=phone,
            email=email,
            password=password,
            address=address,
             )

        return redirect('/')
        
    return render(request,"data.html")



