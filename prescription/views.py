from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from prescription.forms import SignupForm
from django.contrib.auth import authenticate, login, logout
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
        return render(request,'prescription.html')

    def post(self,request):

        return render(request,'prescription.html')

class Result(View):
    def get(self,request):
        return render(request,'results.html')

    # def post(self,request):
    #     return render(request,'results.html')

