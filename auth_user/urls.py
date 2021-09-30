from django.urls import path

from django.views.generic.base import TemplateView

from .views import *

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('', TemplateView.as_view(template_name='auth_user/index.html'), name='index'),
]