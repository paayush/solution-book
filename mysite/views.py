from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, "mysite/index.html")

def signin(request):
    return render(request, "mysite/signin.html")

def signup(request):
    
    if request.method == "post":
        uname = request.post["uname"]
        email1 = request.post["email1"]
        pass1 = request.post["pass1"]
        pass2 = request.post["pass2"]
        email2 = request.post["email2"]
        
        myuser = User.objects.create_user(uname, email1, pass1)
        myuser.save()
        
        messages.success(request, "you account has been created")
        
        return redirect('signin')
        
    return render(request, "mysite/signup.html")