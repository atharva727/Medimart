from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from prescription.forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
import re

from .model import getText, autoCorrect
WORDS= []


# Create your views here.
class Index(View):
    def get(self,request):
        return render(request,'index.html')

class Login(View):
    def get(self,request):
        form = SignupForm()
        context = {'form': form}
        return render(request,'login.html',context)

    def post(self,request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)

        # User Logged in
        if user is not None:
            login(request, user)
            path = request.GET.get('next','/')
            return HttpResponseRedirect(path)

        context = {'error': "Incorrect Email Address or Password"}
        return render(request, "login.html", context)
    
    def logout(request):
        if request.user.is_authenticated:
            logout(request)
            path = request.GET.get('next', '/')
            return redirect(path)
        return redirect("/")

class Signup(View):

    def get(self, request):
        form = SignupForm()
        context = {'form': form}
        return render(request,'login.html',context)

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        
        context = {'form': form}
        return render(request, "login.html", context)

class Prescription(View):
    def get(self,request):
        global WORDS
        with open('./static/medicines.txt','r',encoding="utf8") as f:
            buffer = f.read()
            buffer = buffer.lower()
            WORDS = buffer.split('\n')
        return render(request,'prescription.html')

    def post(self,request):
        #print(request.FILES.get("prescriptionImage"))
        pass

class Result(View):
    def get(self,request):
        return render(request,'results.html')

    def post(self,request):
        request_file=request.FILES['prescriptionImage'] if 'prescriptionImage' in request.FILES else None
        if request_file:
            fs=FileSystemStorage()
            file=fs.save(request_file.name,request_file)
            fileurl=fs.url(file)
            path = '.'+fileurl
            text = getText(path)
            
            MEDICINES = []
            for word in text.split():
                med, sim = autoCorrect(word,WORDS)
                if sim > 0.4:
                    MEDICINES+=[med]
            
        context = {"Medicines":MEDICINES}
        
        return render(request,'results.html',context)
