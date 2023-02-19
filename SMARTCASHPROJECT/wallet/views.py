from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def home(request):
    return render(request, 'registration/home.html')

def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():   
            form.save() 
            username = form.cleaned_data['username']
            #messages.success(request, f"Te has registrado correctamente{username}")        
            return redirect('home')
    else: 
        form = UserRegisterForm()
        
    context = { 'form' : form }     
    return render(request, 'registration/register.html', context)


def login(request):
    
    return render(request,'registration/login.html') #redirigir al login
       
        