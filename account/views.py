from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  
from .forms import UserRegistrationForm

def registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, request.FILES)  
        if user_form.is_valid():
            user_form.save()
            return redirect('registration-done-page')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration.html', {'user_form': user_form})


def registration_done(request):
    return render(request, 'registration_done.html')


# Create your views here.
