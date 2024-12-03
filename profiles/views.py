from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

@login_required
def profile_view(request):
    context = {
        'user': request.user,
        'profile': request.user.profile,
    }
    return render(request, 'profiles.html', context)


