from django.shortcuts import redirect
from django.urls import reverse
from django.db.models import Q
from django.views.generic.edit import UpdateView, DeleteView, CreateView, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from .models import Advert, Platform, ContentType, AdvertCategory, Review, UserProfile
from .forms import AdvertForm, ReviewForm


class ExtraContextMixin:

    def get_advert_category(self):
        return AdvertCategory.objects.all()

    def get_content_type(self):
        return ContentType.objects.all()

    def get_platforms(self):
        return Platform.objects.all()


class AdvertList(ExtraContextMixin, ListView):
    model = Advert
    context_object_name = 'adverts'
    template_name = 'board/main.html'
    paginate_by = 5


class AdvertByPlatformView(ExtraContextMixin, ListView):
    template_name = 'board/main.html'
    context_object_name = 'adverts'
    paginate_by = 5

    def get_queryset(self):
        return Advert.objects.filter(
            platform__name=self.kwargs['platform_name'])


class AdvertAddView(ExtraContextMixin, CreateView):
    """Form view to add new advert object"""
    template_name = 'board/add_advert.html'
    model = Advert
    form_class = AdvertForm
    success_url = '/board'


class AdvertUpdateView(ExtraContextMixin, UpdateView):
    model = Advert
    form_class = AdvertForm
    template_name = 'board/advert_update.html'
    # success_url = '/board/'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.kwargs.get('pk')})


class AdvertDeleteView(ExtraContextMixin, DeleteView):
    """Form view to delete advert"""
    model = Advert
    success_url = '/board'


class AdvertDetailView(DetailView):
    """Single advert detail information"""
    model = Advert
    template_name = 'board/advert_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['reviews'] = Review.objects.filter()


class FilterAdvertsView(ExtraContextMixin, ListView):
    """Adverts filter by 2 parameters"""
    template_name = 'board/main.html'
    context_object_name = 'adverts'

    def get_queryset(self):
        """
        Get lists of 'id' parameters from checkbox form
        in template 'board/main.html.
        Then filter new advert queryset
        """
        queryset = Advert.objects.filter(
            Q(advert_category__in=self.request.GET.getlist(
                'advert_category')) |
            Q(content_type__in=self.request.GET.getlist(
                'content_type'))
        )
        return queryset


class Search(ListView):
    """Поиск обьявлений по названию"""
    paginate_by = 2
    template_name = 'board/main.html'
    context_object_name = 'adverts'

    def get_queryset(self):
        return Advert.objects.filter(
            title__icontains=self.request.GET.get('search'))

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data()
    #     context['search'] = self.request.GET.get('search')
    #     return context


class AddReview(LoginRequiredMixin, View):
    """Add review 'post method' based controller"""
    login_url = 'account_login'

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('detail', pk=kwargs['pk'])

    def get(self, request, *args, **kwargs):

        return redirect('detail', pk=kwargs['pk'])
