from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, "mysite/index.html")

def signin(request):
    return render(request, "mysite/signin.html")

def signup(request):
    
    if request.method == "post":
        uname = request.post["uname"]
        email1 = request.posst["email1"]
        pass1 = request.post["pass1"]
        pass2 = request.post["pass2"]
        email2 = request.post["email2"]
        
        myuser = user.objects.create(uname, email1, pass1)
    return render(request, "mysite/signup.html")