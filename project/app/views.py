from django.shortcuts import render
from.models import Userdata
from.models import Book_data
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
def home(request,em):
    admindata=Userdata.objects.get(email=em)
    fname=admindata.fname
    lname=admindata.lname
    email=admindata.email
    password=admindata.password
    user={
        'fnm':fname,
        'lnm':lname,
        'em':email,
        'pass':password
        }
    return render(request,'home.html',{'user':user})
        
def formdata(request):
    if request.method=='POST':
        doctor=request.POST.get('doctor')
        amount=request.POST.get('amount')
        treat=request.POST.get('treat')
        fnm=request.POST.get('fnm')
        lnm=request.POST.get('lnm')
        em=request.POST.get('em')
        data={
            'doctor':doctor,
            'amount':amount,
            'treat':treat,
            'fnm':fnm,
            'lnm':lnm,
            'em':em,
        }
        return render(request,'formdata.html',{'user':data})
    else:
        return render(request,'home.html')

def datadisplay(request):
    if request.method=='POST':
        fname=request.POST.get('fnm')
        lname=request.POST.get('lnm')
        email=request.POST.get('em')
        doctor=request.POST.get('doctor')
        amount=request.POST.get('amount')
        address=request.POST.get('address')
        contact=request.POST.get('contact')
        treat=request.POST.get('treat')
        date=request.POST.get('date')
        Book_data.objects.create(fname=fname,lname=lname,email=email,doctor=doctor,amount=amount,address=address,contact=contact,treat=treat,date=date)
        data=Book_data.objects.filter(email=email).values()

        admindata=Userdata.objects.get(email=email)
        fname=admindata.fname
        lname=admindata.lname
        email=admindata.email
        password=admindata.password
        user={
            'fnm':fname,
            'lnm':lname,
            'em':email,
            'pass':password
            }
        return render(request,'datadisplay.html',{'data':data,'user':user})
    else:
        return render(request,'formdata.html')

def delete(request,pk,em):
    user=Book_data.objects.filter(id=pk)
    if user:
        user=Book_data.objects.get(id=pk)
        email=user.email
        user.delete()
        data=Book_data.objects.filter(email=email)

        admindata=Userdata.objects.get(email=email)
        fname=admindata.fname
        lname=admindata.lname
        email=admindata.email
        password=admindata.password
        user={
            'fnm':fname,
            'lnm':lname,
            'em':email,
            'pass':password
            }
        return render(request,'datadisplay.html',{'data':data,'user':user})
    else:
        data=Book_data.objects.filter(email=em)

        admindata=Userdata.objects.get(email=em)
        fname=admindata.fname
        lname=admindata.lname
        email=admindata.email
        password=admindata.password
        user={
            'fnm':fname,
            'lnm':lname,
            'em':email,
            'pass':password
            }
        return render(request,'datadisplay.html',{'data':data,'user':user})
def edit(request,pk):
    data=Book_data.objects.get(id=pk)
    myid=data.id
    email=data.email
    address=data.address
    date=data.date
    contact=data.contact 
    edit_data={
        'myid':myid,
        'address':address,
        'date':date,
        'contact':contact,
    }
    alldata=Book_data.objects.filter(email=email)

    admindata=Userdata.objects.get(email=email)
    fname=admindata.fname
    lname=admindata.lname
    email=admindata.email
    password=admindata.password
    user={
        'fnm':fname,
        'lnm':lname,
        'em':email,
        'pass':password
        }
    return render(request,'datadisplay.html',{'data':alldata,'key2':edit_data,'user':user})
def save(request,pk):
    if request.method=='POST':
        address=request.POST.get('address')
        date=request.POST.get('date')
        contact=request.POST.get('contact')
        old_data=Book_data.objects.get(id=pk)
        email=old_data.email
        old_data.address=address
        old_data.date=date
        old_data.contact=contact
        old_data.save()
        alldata=Book_data.objects.filter(email=email) 

        admindata=Userdata.objects.get(email=email)
        fname=admindata.fname
        lname=admindata.lname
        email=admindata.email
        password=admindata.password
        user={
            'fnm':fname,
            'lnm':lname,
            'em':email,
            'pass':password
            }
        return render(request,'datadisplay.html',{'data':alldata,'user':user})


def showdata(request,em):
    email=em 
    getdata=Book_data.objects.filter(email=em)
    if getdata:
        data=Book_data.objects.filter(email=em)
        admindata=Userdata.objects.get(email=em)
        fname=admindata.fname
        lname=admindata.lname
        email=admindata.email
        password=admindata.password
        user={
            'fnm':fname,
            'lnm':lname,
            'em':email,
            'pass':password
            }
        return render(request,'datadisplay.html',{'data':data,'user':user})
    else:
        msg='Data Not Found' 
        admindata=Userdata.objects.get(email=em)
        fname=admindata.fname
        lname=admindata.lname
        email=admindata.email
        password=admindata.password
        user={
            'fnm':fname,
            'lnm':lname,
            'em':email,
            'pass':password
            }
        return render(request,'datadisplay.html',{'msg':msg,'user':user})
