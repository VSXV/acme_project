from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10

class BirthdayCreateView(UserPassesTestMixin, CreateView):
    model = Birthday
    form_class = BirthdayForm

    def test_func(self):
        object = self.get_object()
        return object.author == self.request.user 

class BirthdayUpdateView(UserPassesTestMixin, UpdateView):
    model = Birthday
    form_class = BirthdayForm

    def test_func(self):
        object = self.get_object()
        return object.author == self.request.user 


class BirthdayDeleteView(UserPassesTestMixin, DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:list')
    def test_func(self):
        object = self.get_object()
        return object.author == self.request.user 


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context
