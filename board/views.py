from django.urls import reverse
from django.db.models import Q
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Advert, Platform, ContentType, AdvertCategory
from .forms import AdvertForm


class ExtraContextFuncs:

    def get_advert_category(self):
        return AdvertCategory.objects.all()

    def get_content_type(self):
        return ContentType.objects.all()

    def get_platforms(self):
        return Platform.objects.all()


class AdvertList(ExtraContextFuncs, ListView):
    model = Advert
    context_object_name = 'adverts'
    template_name = 'board/main.html'
    paginate_by = 5


class AdvertByPlatformView(ExtraContextFuncs, ListView):
    template_name = 'board/main.html'
    context_object_name = 'adverts'

    def get_queryset(self):
        return Advert.objects.filter(platform__name=self.kwargs['platform_name'])


class AdvertAddView(ExtraContextFuncs, CreateView):
    """Form view to add new advert object"""
    template_name = 'board/add_advert.html'
    model = Advert
    form_class = AdvertForm
    success_url = '/board'


class AdvertUpdateView(ExtraContextFuncs, UpdateView):
    model = Advert
    form_class = AdvertForm
    template_name = 'board/advert_update.html'
    success_url = '/board/'

    # Переопределить метод для редиректа на by_platform() платформы конкретной записи
    # Не получается достать из object записи имя платформы

    # def get_success_url(self):
    #     return reverse(
    #         'board:by_platform',
    #         kwargs={'platform': self.model.platform}
    #     )


class AdvertDeleteView(ExtraContextFuncs, DeleteView):
    """Form view to delete advert"""
    model = Advert
    success_url = '/board'


class AdvertDetailView(DetailView):
    """Single advert detail information"""
    model = Advert
    template_name = 'board/advert_detail.html'


class FilterAdvertsView(ExtraContextFuncs, ListView):
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
        return Advert.objects.filter(title__icontains=self.request.GET.get('search'))

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data()
    #     context['search'] = self.request.GET.get('search')
    #     return context
