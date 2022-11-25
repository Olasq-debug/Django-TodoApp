from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'user/SignIn.html'
    redirect_authenticated_user = True


    def get_success_url(self):
        return reverse_lazy('home')

class UserRegister(FormView):
    template_name = 'user/Register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
            messages.success(self.request, f'{self.request.user}, your account have been successfully created!', fail_silently= True)
            return redirect('login')
        else:
            messages.error(self.request, 'You have entered wrong credentials', fail_silently= True)
            return redirect('register')
        return super(UserRegister, self).form_valid(form)



