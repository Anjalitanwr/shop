from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm 
from django.contrib import messages
from products.models import Product
from .forms import  ProfileUpdateForm


def home(request):
    return render(request, 'users/home.html') 

# Profile view
@login_required
def profile(request):
    userprofile = request.user
    return render(request, 'users/profile.html',{'userprofile': userprofile})

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('/profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'users/profile_update.html', {'form': form})