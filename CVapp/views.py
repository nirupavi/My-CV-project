from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume
from django.views import View


# Create your views here.


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

