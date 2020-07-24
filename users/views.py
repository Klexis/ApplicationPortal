from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileUpdateForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if email and User.objects.filter(email=email).exists():
                messages.warning(request, f'An account with this e-mail already exists')
                form = UserRegistrationForm()
                return render(request, 'users/register.html', {'form': form})
            newuser = form.save(commit=False)
            newuser.profile = Profile(newuser)
            newuser.save()
            newuser.profile.save()
            is_s = form.cleaned_data.get('is_staff')
            newuser.profile.is_staff = is_s
            newuser.save()
            newuser.profile.save()
            messages.success(request, f'Your Account has been created! YOU can LOG IN')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your Account has been updated!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
