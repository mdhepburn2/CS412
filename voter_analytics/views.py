# File: views.py
# Author: Matthew Hepburn (mhepburn@bu.edu), 10/27/2026
# Description: Views for the voter analytics app. Includes a shared filter view that
#   handles the search form and pagination querystring, a paginated voter list,
#   a single voter detail page, and a graph page that builds Plotly charts
#   (birth year, party affiliation, and election participation) from the filtered voters.

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models.query import QuerySet
from .models import Voter

import plotly
import plotly.graph_objs as go

# Create your views here.

class VoterFilterView(ListView):
    '''class to be inherited by anything that filters voters'''
    model = Voter
    def get_context_data(self, **kwargs):
        '''add filter queries to context'''
        context = super().get_context_data(**kwargs)

        parties = ['U ','D ','R ','J ','A ','CC','X ','L ','Q ','S ','FF','G ','HH','T ','AA','GG','Z ','O ','P ','E ','V ','H ','Y ','W ','EE','K ']

        years = [str(y) for y in range(1913,2005)]
        years.reverse()

        scores = [str(i) for i in range(0,6)]

        context['parties'] = parties
        context['years'] = years
        context['scores'] = scores

        # get the query minus page so its not lost on a page turn
        query = self.request.GET.copy()
        query.pop('page', None)
        context['querystring'] = query.urlencode()
        

        return context

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

        if 'voter_score' in self.request.GET:
            voter_score = self.request.GET.get('voter_score')
            if voter_score:
                voters = voters.filter(voter_score=voter_score)

        if 'v20state' in self.request.GET:
            voters = voters.filter(v20state=True)

        if 'v21town' in self.request.GET:
            voters = voters.filter(v21town=True)

        if 'v21primary' in self.request.GET:
            voters = voters.filter(v21primary=True)

        if 'v22general' in self.request.GET:
            voters = voters.filter(v22general=True)

        if 'v23town' in self.request.GET:
            voters = voters.filter(v23town=True)

        return voters

class VotersListView(VoterFilterView):
    '''view to display voter data'''

    model = Voter
    template_name = 'voter_analytics/voters.html'
    context_object_name = 'voters'
    paginate_by = 100 # how many voters per page

class VoterDetailView(DetailView):
    '''view to show one voter'''

    model = Voter
    context_object_name = 'voter'
    template_name = 'voter_analytics/show_voter.html'


class GraphView(VoterFilterView):
    '''view to show graphs from aggregate data'''

    model = Voter
    context_object_name = 'voters'
    template_name = 'voter_analytics/graphs.html'

    def get_context_data(self, **kwargs):
        '''add the graphs to context'''
        context = super().get_context_data(**kwargs)
        voters = self.get_queryset()

        ## make the bar plot of birth years
        yearsX = [i for i in range(1913,2006)]
        yearsY = [voters.filter(date_of_birth__year=i).count() for i in yearsX]

        yearsBar = go.Bar(x=yearsX,y=yearsY)
        years_title_text = f'Voter Distribution by Year of Birth (n = {voters.count()})'
        yearsDiv = plotly.offline.plot({'data': [yearsBar],
                                      "layout_title_text": years_title_text},
                                      auto_open=False,
                                      output_type='div')
        context['bardiv'] = yearsDiv

        ## make the pie chart of parties
        partyLabels = context.get('parties')
        partyValues = [voters.filter(party_affiliation=party).count() for party in partyLabels]
        party_title_text = f'Voter Distribution by Party Affiliation (n = {voters.count()})'

        partyPie = go.Pie(labels=partyLabels,values=partyValues)
        partyDiv = plotly.offline.plot(
            {'data': [partyPie],
             'layout_title_text': party_title_text},
             auto_open=False,
             output_type='div'
        )
        context['partyDiv'] = partyDiv

        ## make the bar chart of election vote counts
        electionsX = ['v20state','v21town','v21primary','v22general','v23town']
        electionsY = [voters.filter(v20state=True).count()]
        electionsY += [voters.filter(v21town=True).count()]
        electionsY += [voters.filter(v21primary=True).count()]
        electionsY += [voters.filter(v22general=True).count()]
        electionsY += [voters.filter(v23town=True).count()]

        elections_title_text = f'Vote Count by Election (n = {voters.count()})'

        electionsBar = go.Bar(x=electionsX, y=electionsY)
        electionsDiv = plotly.offline.plot(
            {'data': [electionsBar],
             'layout_title_text': elections_title_text},
            auto_open=False,
            output_type='div'
        )
        context['electionsDiv'] = electionsDiv


        return context
