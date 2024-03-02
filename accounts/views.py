from django.shortcuts import render

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