from django.shortcuts import render, reverse
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Advert, Platform
from .forms import AdvertForm


class AdvertList(View):

    def get(self, request):
        adverts = Advert.objects.all()
        platforms = Platform.objects.all()
        context = {'adverts': adverts, 'platforms': platforms}
        return render(request, 'board/main.html', context=context)


class AdvertByPlatformView(ListView):
    template_name = 'board/main.html'
    context_object_name = 'adverts'

    def get_queryset(self):
        return Advert.objects.filter(
            platform__name=self.kwargs['platform_name']
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['platforms'] = Platform.objects.all()

        return context


class AdvertAddView(FormView):
    template_name = 'board/add_advert.html'
    form_class = AdvertForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['platforms'] = Platform.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self):
        return reverse(
            'board:by_platform',
            kwargs={'rubric_name': self.object.cleaned_data['rubric'].name}
        )


class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'board/advert_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['platforms'] = Platform.objects.all()
        return context
