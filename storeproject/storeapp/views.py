from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from storeapp.models import Register, Dept, Course

def demo(request):
    obj = Dept.objects.all()
    return render(request,'home.html',{'key1' : obj})
def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['psw']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('storeapp:order')
        else:
            messages.warning(request, "Invalid user")

    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['psw']
        password2 = request.POST['psw2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                #return redirect('register')
            else :
                user1 = User.objects.create_user(username=username,password=password)
                user1.save()
                return redirect('storeapp:login')
        else :
            messages.info(request,"Password not matching")
            #return redirect('register')

    return render(request,'register.html')

def order(request):
    Deptobj = Dept.objects.all()
    Courseobj = Course.objects.all()
    if request.method == 'POST':

        messages.info(request, "Data sent successfully")
        return redirect('storeapp:order')
    return render(request, 'order.html', {'Deptobj': Deptobj, 'Courseobj':Courseobj})
def logout(request):
    return redirect('/')

def load_course(request):
    pass