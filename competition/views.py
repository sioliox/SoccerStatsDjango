from django.views.generic import DetailView, ListView

from .models import Competition


class CompetitionDetailView(DetailView):
    model = Competition
    context_object_name = 'competition'


class CompetitionListView(ListView):
    model = Competition
    context_object_name = 'competitions'
