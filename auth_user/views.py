from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from random import randrange
from .models import CodeGenery
from django.core.mail import send_mail
from auth_project.settings import EMAIL_HOST_USER


class SignUp(APIView):
    def post(self, request):
        print(request.data)
        create = get_user_model().objects.create(**request.data)
        genery_code = CodeGenery.objects.create(code=randrange(1000, 9999), user=create)
        subject = "U have got a password code"
        message = f'here is ur code {genery_code}'
        send_from = EMAIL_HOST_USER
        send_to = request.POST.get("email")
        send_mail(subject=subject, message=message, from_email=send_from, recipient_list=[send_to])
        return Response(200)
