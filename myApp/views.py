from django.http import HttpResponse
from django.shortcuts import redirect, render
from myApp.forms import LoginForms, SignupForms, StudentsForms
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from myApp.models import Students
# Create your views here.

def signupPage(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            form=SignupForms(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'signup succeccfully login')
                return redirect("login")
            else:
                messages.error(request,"signup error")
        else:        
            form=SignupForms()   
        return render(request,"signup.html",{'form':form})
    else:
        return redirect('home')
def loginPage(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form=LoginForms(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user:
                    login(request,user)
                    messages.success(request,"login succefully")
                    return redirect("home")
            else:
                messages.error(request,"login fail try more then")
                return redirect("login")
        else:
            form=LoginForms()        
        return render(request,"login.html",{'form':form})
    else:
        return redirect("home")

def homePage(request):
    students=Students.objects.all()
    
    return render(request,"home.html",{"students":students})

def logoutPage(request):
    logout(request)
    return redirect("login")

def addpage(request):
    if request.method =="POST":
        form = StudentsForms(request.POST,request.FILES)
        if form.is_valid():
           form.save()
           messages.success(request,"student add succecfully")
           return redirect("home")
        else:
            messages.error(request,"student error")
            return redirect("add")
    else:    
     form=StudentsForms()
     return render(request,"add.html",{"form":form})
 
def editPage(request,id):
    if request.method == "POST":
        student=Students.objects.get(id=id)
        form=StudentsForms(request.POST,instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,"update scceccfull")
            return redirect("home")
        else:
            messages.error(request,'failed to update')
            return redirect('edit')
    else:
        
        student=Students.objects.get(id=id)
        form=StudentsForms(instance=student)
    
    return render(request,"edit.html",{"form":form})

def deleteStudent(request,id):
    student=Students.objects.get(id=id)
    student.delete()
    return redirect("home")