from django.shortcuts import render,redirect

from accounts.forms import *
from accounts.models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def login_view(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def admin_home(request):
    return render(request,'admintemp/index.html')

def customer_home(request):
    return render(request,'customertemp/index.html')

def worker_home(request):
    return render(request,'workertemp/index.html')

def worker_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 2
            user.is_active = True
            user.save()
            return redirect('workers') 
    else:
        form = UserRegistrationForm()
    return render(request, 'admintemp/worker_register.html', {'form': form})

def customer_signup(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        u_form = UserRegistrationForm(request.POST)
        if form.is_valid() and u_form.is_valid():
            user = u_form.save(commit=False)
            user.role = 3
            user.is_active = True
            user.save()
            customer = form.save(commit=False)
            customer.user = user
            customer.save()
            return redirect('sign-in') 
    else:
        form = CustomerRegistrationForm()
        u_form = UserRegistrationForm()
    return render(request,'register.html',{'form':form,'u_form':u_form})

def worker_view(request):
    data = User.objects.filter(role=2)
    return render(request, 'admintemp/worker_view.html',{'data':data})

def customer_view(request):
    data = User.objects.get(role=3)
    c_data = UserProfile.objects.filter(user__in=data)
    return render(request, 'admintemp/customer_view.html',{'c_data':c_data})