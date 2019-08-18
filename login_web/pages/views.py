# pages/views.py
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate

from users.forms import CustomUserCreationForm
from django.shortcuts import render, redirect




class HomePageView(TemplateView):
    template_name = 'home.html'


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})