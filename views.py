from django.shortcuts import render
from . models import Userreg,Login,Addfood,Addfoodcategories,Addchef,Tableset,Tablereservation
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def log(request):
    m = Login.objects.get(username=request.POST['username'],password=request.POST['password'])
    if m.status == 0:
        return render(request,'adminhome.html')
    elif m.status == 1:
        request.session['User'] = m.username
        return render(request, 'uhome.html')
    elif m.status==2:
        return render(request,'chefhome.html')
    else:
        return render(request,'login.html')
def ureg(request):
     return render(request,'ureg.html')
def reg(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    address = request.POST['address']
    username = request.POST['uname']
    password = request.POST['password']
    data=Userreg(name=name,email=email,phone=phone,address=address,username=username)
    data.save()
    data1=Login(username=username,password=password,status=1)
    data1.save()
    return render(request,'login.html')
def uhome(request):
    data1 = Addfood.objects.all()
    return render(request,'uhome.html',{'f':data1})
def add(request):
    return render(request,'add.html')
def show(request):
    return render(request,'show.html')
def report(request):
    return render(request,'report.html')
def addfood(request):
    return render(request,'addfood.html')
def afood(request):
    food = request.POST['food']
    price = request.POST['price']
    description = request.POST['description']
    category = request.POST['category']
    photo = request.FILES['file']
    fooddata = Addfood(food=food,price=price,description=description,category=category,photo=photo)
    fooddata.save()
    return render(request,'addfood.html')
def price(request):
    return render(request,'price.html')
def description(request):
    return render(request,'description.html')
def category(request):
    return render(request,'category.html')
def category1(request):
    return render(request,'category1.html')
def fcategories(request):
    name = request.POST['category']
    cfooddata = Addfoodcategories(name=name)
    cfooddata.save()
    return render(request,'category1.html')
def foodview(request):
    data=Addfood.objects.all()
    return render(request,'foodview.html',{'d':data})
def categoryview(request):
    data=Addfoodcategories.objects.all()
    return render(request,'categoryview.html',{'d':data})
def edit(request):
    id=request.POST['id']
    data=Addfood.objects.get(id=id)
    return render(request,'edit.html',{'data':data})
def update(request):
    id = request.POST['id']
    data=Addfood.objects.get(id=id)
    data.price=request.POST['price']
    data.description=request.POST['description']
    data.category=request.POST['category']
    data.save()
    data1=Addfood.objects.all()
    return render(request,'foodview.html',{'d':data1})
def addchef(request):
    return render(request,'addchef.html')
def achef(request):
    name = request.POST['name']
    email = request.POST['email']
    designation = request.POST['designation']
    photo = request.FILES['file']
    chefdata = Addchef(name=name,email=email,designation=designation,photo=photo)
    chefdata.save()
    return render(request,'addchef.html')
def foodlist(request):
    data = Addfood.objects.all()
    return render(request, 'foodlist.html', {'d': data})

def reservation(request):
    return render(request,'reservations.html')
def tableset(request):
    return render(request,'reservations.html')
def tset(request):
    tablename = request.POST['tablename']
    tablesize = request.POST['tablesize']
    tabledata = Tableset(tablename=tablename,tablesize=tablesize)
    tabledata.save()
    return render(request, 'reservations.html')
def fooddetails(request):
    id=request.POST['id']
    data=Addfood.objects.get(id=id)
    return render(request,'fooddetails.html',{'data':data})
def reservationreport(request):
    return render(request,'reservationreport.html')
def ser(request):
    n=request.POST['food']
    data=Addfood.objects.filter(food=n)
    return render(request,'about.html',{'data':data})
def about(request):
        return render(request, 'about.html')
def det(request):
        id=request.POST['id']
        data=Addfood.objects.filter(id=id)
        return render(request, 'det.html',{'data':data})
def ntablereservation(request):
    return render(request,'tablereservation.html')
def tablereservation(request):
    guests = request.POST['guest']
    email = request.POST['email']
    username = request.POST['username']
    date = request.POST['date']
    time = request.POST['time']
    data = Tablereservation(guest=guests,email=email,username=username,date=date,time=time)
    data.save()
    return render(request,'tablereservation.html')














