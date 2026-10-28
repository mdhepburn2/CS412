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

    def get_queryset(self):
        '''limit the queryset'''
        voters = super().get_queryset()

        if 'party' in self.request.GET:
            party = self.request.GET.get('party')
            if party:
                voters = voters.filter(party_affiliation=party)

        if 'min_dob' in self.request.GET:
            min_dob = self.request.GET.get('min_dob')
            if min_dob:
                voters = voters.filter(date_of_birth__year__gte=int(min_dob))

        if 'max_dob' in self.request.GET:
            max_dob = self.request.GET.get('max_dob')
            if max_dob:
                voters = voters.filter(date_of_birth__year__lte=int(max_dob))

        return voters

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        parties = ['U ','D ','R ','J ','A ','CC','X ','L ','Q ','S ','FF','G ','HH','T ','AA','GG','Z ','O ','P ','E ','V ','H ','Y ','W ','EE','K ']
        
        years = [str(y) for y in range(1920,2005)]
        years.reverse()

        context['parties'] = parties
        context['years'] = years



        # get the query minus page so its not lost on a page turn
        query = self.request.GET.copy()
        query.pop('page', None)
        context['querystring'] = query.urlencode()
        

        return context
