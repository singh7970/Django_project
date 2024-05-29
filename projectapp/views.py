from django.shortcuts import render,redirect,HttpResponse

from .models import Basicform,DATA,Insta


# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        print(name,email,phone,address)
        #save data to the database
        Basicform.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address
             )

        return redirect('/')

    return render(request,"index.html")

def delete(request,contact_id):
    dele=Basicform.objects.get(id=contact_id)
    dele.delete()
    return redirect('showall')
def delete_data(request,data_id):
    delet=DATA.objects.get(id=data_id)
    delet.delete()
    return redirect('showall')


def showall(request):
    show=Basicform.objects.all()
    data=DATA.objects.all()
    inta=Insta.objects.all()

    Synt={"show":show,"data":data,"inta":inta}
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
        print(name)
        
        DATA.objects.create(
            name=name,
            phone=phone,
            email=email,
            password=password,
            address=address,
             )

        return redirect('/')
        
    return render(request,"data.html")


def insta(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        Insta.objects.create(
            username=username,
            password=password,
        )
        return render(request,"extra.html")

    return render(request,'insta.html')
def delete_insta(request,insta_id):
    intadele=Insta.objects.get(id=insta_id)
    intadele.delete()


    return redirect('showall')








