from django.shortcuts import render
from django.views.generic import ListView
from django.db.models.query import QuerySet
from .models import Voter

# Create your views here.

class VotersListView(ListView):
    '''view to display voter data'''

    model = Voter
    template_name = 'voter_analytics/voters.html'
    context_object_name = 'voters'
    paginate_by = 100 # how many voters per page

    # def get_queryset(self):
    #     '''limit the queryset'''
    #     voters = super().get_queryset()
    #     return voters[:25]
