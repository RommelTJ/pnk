from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import PNKEmployeeForm
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


def join(request):
    return render(request, 'join.html', {})
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
#########################
# End Services Views    #
#########################


#########################
# Start Knowledge Views #
#########################
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

    def get(self, request, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        if request.user.is_authenticated:
            employee = PNKEmployee.objects.filter(user__exact=request.user).first()
            if employee:
                context['pnk_employee'] = employee
            else:
                context['pnk_employee'] = None
        else:
            context['pnk_employee'] = None
        return render(request, 'index.html', context)


class PNKProfileCreateView(CreateView):
    template_name = 'pnk_profile_create.html'
    form_class = PNKEmployeeForm
    success_url = reverse_lazy('team')

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context.get('pnk_employee') is None:
            form = PNKEmployeeForm()
            return render(request, self.get_template_name(), {'form': form})
        return render(request, self.get_template_name(), context)

    def post(self, request, *args, **kwargs):
        form = PNKEmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.emp_no = generate_next_emp_no()
            self.object.user = self.request.user
            self.object.type = 'AFF'
            self.object.save()
            return HttpResponseRedirect('/team/')
        return render(request, self.template_name, {'form': form})

    def get_template_name(self):
        return self.template_name

    def get_context_data(self):
        return {
            'pnk_employee': self.get_employee(),
        }

    def get_employee(self):
        return PNKEmployee.objects.filter(user__exact=self.request.user).first()


class ProfileDetailView(DetailView):
    template_name = 'profile_detail.html'
    model = PNKEmployee

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        return context


class ProfileListView(ListView):
    model = PNKEmployee
    template_name = 'team.html'
    paginate_by = 10

    def get_queryset(self):
        order_by_field = self.request.GET.get('order-by') or 'hire_date'
        queryset = super(ProfileListView, self).get_queryset()
        return queryset.order_by(order_by_field)

#########################
# End Class Based Views #
#########################