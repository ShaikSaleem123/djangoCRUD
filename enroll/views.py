import email
from django.shortcuts import render,HttpResponse
from enroll.models import User
from .forms import StudentRegistration
from django.contrib import messages
# Create your views here.

#this function will add new item in the data base
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg = User(name=nm,email=em)
            if int(pw) == 5864: #if entered paswd is 5864 then only data will be stored saved
                reg.save()
                messages.success(request, 'Your data Saved...!')
                fm = StudentRegistration() #after saving it form will get blank to take new
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/addandshow.html',{'form':fm})

#this function read and show the stored data on the web page
def show(request):
    db=User.objects.all()
    return render(request,'enroll/show.html',{'db':db})

# this function will delete the record from data base
def delete(request,id):
    if request.method == 'POST':
        dl = User.objects.get(pk=id)
        dl.delete()
        return HttpResponse('record is deleted')

#this function will update the existing records

def update(request,id):
    
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        if int(pw) == 5864:
            messages.success(request, 'Your data Saved...!')
        
    context ={'form':fm}
    return render(request,'enroll/update.html',context)

'''
def update(request,id):
    upd = User.objects.filter(pk=id)
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        print("hello")
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            reg = User(name=nm,email=em)
            print("hello")
            reg.save()
        else:
            fm = StudentRegistration()


    return render(request,'enroll/update.html',{'upd':upd})
'''
