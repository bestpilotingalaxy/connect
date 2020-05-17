from django.shortcuts import render, reverse
from django.views.generic.edit import UpdateView, DeleteView, CreateView
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
        return Advert.objects.filter(platform__name=self.kwargs['platform_name'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['platforms'] = Platform.objects.all()

        return context


class AdvertAddView(CreateView):
    template_name = 'board/add_advert.html'
    model = Advert
    form_class = AdvertForm


class AdvertUpdateView(UpdateView):
    model = Advert
    form_class = AdvertForm
    template_name = 'board/advert_update.html'
    success_url = '/board/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['platforms'] = Platform.objects.all()
        return context

    # Переопределить метод для редиректа на by_platform() платформы конкретной записи
    # Не получается достать из object записи имя платформы

    # def get_success_url(self):
    #     return reverse(
    #         'board:by_platform',
    #         kwargs={'platform': self.model.platform.name}
    #     )


class AdvertDeleteView(DeleteView):
    model = Advert
    success_url = '/board'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['platforms'] = Platform.objects.all()
        return context


class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'board/advert_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['platforms'] = Platform.objects.all()
        return context
