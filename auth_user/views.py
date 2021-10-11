from django.urls import reverse
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate
from .models import CodeGenery
from django.conf import settings
from random import randrange
from django.core.mail import send_mail


class SignUp(APIView):
    def post(self, request):
        create = get_user_model().objects.create_user(**request.data)
        user = authenticate(email=request.data['email'], password=request.data['password'])
        genery_code = CodeGenery.objects.create(code=randrange(1000, 9999), user=create)
        subject = "U have got a password code"
        message = f'here is ur code {genery_code}'
        send_from = settings.EMAIL_HOST_USER
        send_to = request.data['email']
        send_mail(subject=subject, message=message, from_email=send_from, recipient_list=[send_to])
        if user:
            login(request, user)
        return HttpResponseRedirect(reverse('activate'))


class VerifyView(APIView):
    def post(self, request):
        print(type(request.user))
        if request.data['code'] == CodeGenery.objects.get(user_id=request.user.id).code:
            user = request.user
            user.is_verified = True
            user.save()
            return HttpResponse(f'<h1>hi, {request.user.first_name} </h1>')
        return HttpResponseRedirect(reverse('activate'))

# def activate(request):
#
#     return HttpResponse(f'<h1>hi, {request.user.first_name}</h1>')
