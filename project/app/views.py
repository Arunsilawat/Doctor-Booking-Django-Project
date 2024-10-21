from django.shortcuts import render
from.models import Userdata
# Create your views here.

def register(request):
    return render(request,'register.html')
def register(request):
    if request.method=='POST':
        fname=request.POST.get('firstName')
        lname=request.POST.get('lastName')
        email=request.POST.get('email')
        password=request.POST.get('password')
        use=Userdata.objects.filter(email=email)
        if use:
            msg="Email Id Already Exist"
            return render(request,'register.html',{'msg':msg})
        else:
            msg="Registration Successfull"
            Userdata.objects.create(fname=fname,lname=lname,email=email,password=password)
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'register.html')
def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password1=request.POST.get('password')
        user=Userdata.objects.filter(email=email)
        if user:
            admindata=Userdata.objects.get(email=email)
            fname=admindata.fname
            lname=admindata.lname
            email=admindata.email
            password=admindata.password
            if password==password1:
                user={
                    'fnm':fname,
                    'lnm':lname,
                    'em':email,
                    'pass':password
                }
                return render(request,'home.html',{'user':user})
            else:
                msg="Password Not Matched"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="Email Id Not Registered"
            return render(request,'login.html',{'msg':msg})
    return render(request,'login.html')
def home(request):
    return render(request,'home.html')