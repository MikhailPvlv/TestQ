from django.shortcuts import render
from .forms import SubscribeForm
from auth_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.views import generic
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


# def subscribe(request):
#     sub = SubscribeForm
#     if request.method == 'POST':
#         sub = SubscribeForm(request.POST)
#         subject = 'HI BOYS'
#         message = "u`ll be enjoyed"
#         recepient = str(sub['Email'].value())
#         send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
#         return render(request, 'success/html', {'recepient': recepient})
#     return render(request, 'layout/html', {'form': sub})


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = 'auth_user/index.html'
    template_name = 'auth_user/signup.html'
