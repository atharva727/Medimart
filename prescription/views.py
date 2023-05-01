from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from prescription.forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage

import warnings
warnings.filterwarnings("ignore")

import os
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from .webscraping import *
from doctr.models import ocr_predictor
from .textRecognition import getText, autoCorrect
WORDS= []
model = None

# Create your views here.
class Index(View):
    def get(self,request):
        global model
        if model is None:
            print("Model Loaded")
            model = ocr_predictor(pretrained=True)
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
        pass

class Result(View):
    def get(self,request):
        return render(request,'results.html')

    def post(self,request):
        global model
        request_file=request.FILES['prescriptionImage'] if 'prescriptionImage' in request.FILES else None
        if request_file is not None:
            fs=FileSystemStorage()
            file=fs.save(request_file.name,request_file)
            fileurl=fs.url(file)
            path = '.'+fileurl            
            text = getText(path,model)

            MEDICINES = []
            for word in text.split():
                med, sim = autoCorrect(word,WORDS)
                if sim > 0.4:
                    MEDICINES+=[med]
        
            options = Options()
            options.add_argument('--headless=new')

            driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
            webs = []
            data = [
                getPharmeasy(MEDICINES,driver),
                getApollo(MEDICINES,driver),
                getNetmed(MEDICINES,driver)
            ]
            os.remove(path)
            
        context = {"data":data,'webs':webs}
                
        return render(request,'results.html',context)
