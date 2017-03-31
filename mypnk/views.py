from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import PNKEmployee, generate_next_emp_no


def giveaway(request):
    return render(request, 'giveaway.html', {})


#########################
# Start About Views     #
#########################
def about(request):
    return render(request, 'about.html', {})


def vision(request):
    return render(request, 'vision.html', {})


def values(request):
    return render(request, 'values.html', {})


def team(request):
    return render(request, 'team.html', {})


def benefits(request):
    return render(request, 'benefits.html', {})


def bylaws(request):
    return render(request, 'bylaws.html', {})


def partners(request):
    return render(request, 'partners.html', {})


def join_pnk(request):
    return render(request, 'join-pnk.html', {})
#########################
# End About Views       #
#########################


#########################
# Start Solutions Views #
#########################
def mission_planner(request):
    return render(request, 'mission-planner.html', {})


def fleet_view(request):
    return render(request, 'fleet-view.html', {})
#########################
# End Solutions Views   #
#########################


#########################
# Start Services Views  #
#########################
def fuel_services(request):
    return render(request, 'fuel-services.html', {})


def maintenance_repair(request):
    return render(request, 'maintenance-and-repair.html', {})


def transportation(request):
    return render(request, 'transportation.html', {})


def implementation(request):
    return render(request, 'implementation.html', {})


def support_training(request):
    return render(request, 'support-and-training.html', {})


def consulting_services(request):
    return render(request, 'consulting-services.html', {})


def professional_services(request):
    return render(request, 'professional-services.html', {})
#########################
# End Services Views    #
#########################


#########################
# Start Knowledge Views #
#########################
def pnk_podcast(request):
    return render(request, 'pnk-podcast.html', {})


def links_tools(request):
    return render(request, 'links-and-tools.html', {})
#########################
# End Knowledge Views   #
#########################


#########################
# Class Based Views     #
#########################

class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['pnk_employee'] = 'Rommel'
        # PNKEmployee.objects.filter(emp_no__exact=self.object.emp_no)
        # TODO: Check if user is a PNKEmployee
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


class ProfileDetailView(DetailView):
    template_name = 'profile_detail.html'
    model = PNKEmployee

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        return context

#########################
# End Class Based Views #
#########################