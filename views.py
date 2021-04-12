from django.shortcuts import render
from . models import Userreg,Login,Addfood,Addfoodcategories
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def log(request):
    m = Login.objects.get(uname=request.POST['uname'],password=request.POST['password'])
    if m.status == 0:
        return render(request,'adminhome.html')
    elif m.status == 1:
        request.session['user'] = m.username
        return render(request, 'uhome.html')
    elif m.status==2:
        return render(request='adminhome.html')
    else:
        return render(request,'login.html')
def ureg(request):
     return render(request,'ureg.html')
def reg(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    address = request.POST['address']
    uname = request.POST['uname']
    password = request.POST['password']
    data=Userreg(name=name,email=email,phone=phone,address=address,uname=uname)
    data.save()
    data1=Login(uname=uname,password=password,status=1)
    data1.save()
    return render(request,'login.html')
def uhome(request):
    return render(request,'uhome.html')
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
    fooddata = Addfood(food=food,price=price,description=description,category=category)
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

# Create your views here.
