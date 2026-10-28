from django.urls import path
from django.conf import settings
from . import views
from .views import *

urlpatterns = [
    path('', VotersListView.as_view(), name='home'),
    path('voters', VotersListView.as_view(), name='voters_list'),
]