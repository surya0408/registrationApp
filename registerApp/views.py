from django.shortcuts import render
from registerApp.forms import UserForm
from django.contrib.auth import login,authenticate

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"registerApp/welcome.html",{'form':form})
    return render(request,'registerApp/register.html',{'form':form})