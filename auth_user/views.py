from django.shortcuts import render
from .forms import SubscribeForm
from auth_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.views import generic
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model


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


class SignUp(APIView):
    def post(self, request):
        print(request.data)
        get_user_model().objects.create(**request.data)

        return Response(200)
