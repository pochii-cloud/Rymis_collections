from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from core.forms import RegisterUserForm, ProfileForm


class RegisterUser(View):
    def get(self, request):
        form = RegisterUserForm()
        profile_form = ProfileForm(request.POST)
        context = {'form': form, 'profile_form': profile_form}
        return render(request, 'Register.html', context)

    def post(self, request):
        form = RegisterUserForm(request.POST)
        profile_form = ProfileForm(request.POST, files=request.FILES)
        context = {'form': form, 'profile_form': profile_form}
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.info(request, 'account created successfully')
            return redirect('LoginPage')
        else:
            messages.error(request, 'invalid inputs!!.Note that all fields are case sensitive')
        return render(request, 'Register.html', context)


class LoginPage(LoginView):
    template_name = 'login.html'


class LogoutPage(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('LoginPage')


class ProfilePage(View):
    def get(self, request):
        form = RegisterUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, files=request.FILES, instance=request.user.profile)
        context = {'form': form, 'profile_form': profile_form}
        return render(request, 'profilepage.html', context)

    def post(self, request):
        form = RegisterUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, files=request.FILES, instance=request.user.profile)
        context = {'form': form, 'profile_form': profile_form}
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'You updated your profile successfully')
        return render(request, 'profilepage.html', context)