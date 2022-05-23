from django.shortcuts import render,redirect
from .forms import ResumeForm
from .models import Resume
from django.views import View
from .forms import signupform
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup_page(request):
    if request.method == 'POST':
        fm = signupform(request.POST)
        print('This is post method')
        if fm.is_valid():
            username = fm.cleaned_data.get('username')
            email = fm.cleaned_data.get('email')
            print(username)
            print(email)
            fm.save()
            #messages.success(request,'Account created successfully')
            messages.success(request, f'Your account has been created ! You are now able to log in')
            #return redirect('login')
    else:
        fm = signupform()
        print('This is get method')
    return render(request,'CVapp/signup.html',{'form':fm})

def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request,data=request.POST)

        if fm.is_valid():
            print('fm is valid')
            uname = fm.cleaned_data['username']
            #uemail = fm.cleaned_data['email']
            upass = fm.cleaned_data['password']
            user = authenticate(request,username=uname,password=upass)
            print('user')
            if user is not None:
                login(request,user)
                print('Sucessfully')
                messages.success(request,'Logged in successfully')
                return redirect('cvmaker')

    else:
        fm = AuthenticationForm()
        print('This is GET method')
    return render (request,'CVapp/loginpage.html',{'form':fm})

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login')

class Homeview(View):
    def get(self,request):
        form = ResumeForm()
        users = Resume.objects.all()
        return render(request,'CVapp/home.html',{'users':users,'form':form})

    def post(self,request):
        form = ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'CVapp/home.html',{'form':form})
class resumeview(View):
    def get(self,request,pk):
         user = Resume.objects.get(pk=pk)
         return render(request,'CVapp/view.html',{'user':user})


def update_data(request,id):
    if request.method == 'POST':
        pi = Resume.objects.get(pk=id)
        fm = ResumeForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi = Resume.objects.get(pk=id)
        fm = ResumeForm(instance=pi)
    return render(request,'CVapp/update.html',{'form':fm})

def delete_data(request,id):
    if request.method == 'POST':
        pi = Resume.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/cvmaker/')


def change_pass(request):
    if request.method == 'POST':
      fm = PasswordChangeForm(user=request.user,data=request.POST)
      if fm.is_valid():
        fm.save()
        update_session_auth_hash(request,fm.user)
        return HttpResponseRedirect('/login/')

    else:
      fm = PasswordChangeForm(user=request.user)
    return render(request,'CVapp/changepassword.html',{'form':fm})

