from django.shortcuts import render

def homepage(request):
    return render(request,"home.html")

def indexpage(request):
    return render(request,"index.html")

def aboutuspage(request):
    return render(request,"about.html")

def resumepage(request):
    return render(request,"createprofile.html")


def registrationpage(request):
    return render(request,"registration.html")

def contactuspage(request):
    return render(request,"contactus.html")

def loginpage(request):
    return render(request,"login.html")