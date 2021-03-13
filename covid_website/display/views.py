from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
def hospital(request):
    return render(request,'hospitail_detail.html')
def survey(request):
    return render(request,'survey.html')