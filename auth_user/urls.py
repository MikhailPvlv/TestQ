from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('signup/activate/', VerifyView.as_view(), name='activate'),
    path('', TemplateView.as_view(), name='index')

]