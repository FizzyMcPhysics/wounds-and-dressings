from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from braces.views import LoginRequiredMixin
from django_filters.views import FilterView

from .filters import DressingFilter
from .models import Wound, Dressing, WOUND_TYPE, WOUND_DEPTH
from .forms import WoundForm


class AuthoredMixin(object):
    def form_valid(self, form):
        if hasattr(form, "instance"):
            form.instance.user = self.request.user
        return super(AuthoredMixin, self).form_valid(form)


# Create your views here.
class WoundListView(ListView):
    model = Wound


class DressingListView(ListView):
    model = Dressing


class DressingDetailView(DetailView):
    model = Dressing


class DressingFilterView(FilterView):
    filterset_class = DressingFilter 


class WoundCreateView(LoginRequiredMixin, AuthoredMixin, CreateView):
    model = Wound
    form_class = WoundForm

    def get_success_url(self):
        return "{url}?wound=1&absorbancy={absorb}&body_area=&body_area={body}&diabetic_safe={diabetes}&anti_microbial={infected}&suitable_for={type}&deep_wounds={deep}&debriding={debriding}".format(
            url=reverse("dressing_filter"),
            absorb=self.object.exudate_level,
            body=self.object.body_area,
            diabetes=self.object.diabetic_patient,
            infected=1 if self.object.wound_type.short_name==WOUND_TYPE.infected else 0,
            type=self.object.wound_type.id,
            deep=0 if self.object.wound_depth==WOUND_DEPTH.shallow else 1, 
            debriding=1 if self.object.wound_type.short_name==WOUND_TYPE.black else 0,
        )
