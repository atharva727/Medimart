from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from prescription.forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from doctr.models import ocr_predictor
from doctr.io import DocumentFile





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
        #print(request.FILES.get("prescriptionImage"))
        request_file=request.FILES['prescriptionImage'] if 'prescriptionImage' in request.FILES else None
        if request_file:
            fs=FileSystemStorage()
            file=fs.save("Atharva.jpg",request_file)
            fileurl=fs.url(file)
            doc = DocumentFile.from_images("C:/Users/anjug/Downloads/car5.jpg")
            model = ocr_predictor(pretrained=True)
            result = model(doc)
            
        return render(request,'prescription.html')

class Result(View):
    def get(self,request):
        return render(request,'results.html')

    # def post(self,request):
    #     return render(request,'results.html')

