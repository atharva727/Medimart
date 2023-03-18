from django.shortcuts import render
from django.views import View

# Create your views here.
class Index(View):
    def get(self,request):
        return render(request,'index.html')

class Login(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        return render(request,'login.html')

class Prescription(View):
    def get(self,request):
        return render(request,'prescription.html')

    def post(self,request):
        return render(request,'prescription.html')

class Result(View):
    def get(self,request):
        return render(request,'results.html')

    def post(self,request):
        return render(request,'results.html')

