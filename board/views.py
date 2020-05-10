from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views.generic.base import View

from .models import Advert, Platform
from .forms import AdvertForm


class AdvertList(View):

    def get(self, request):
        adverts = Advert.objects.all()
        platforms = Platform.objects.all()
        context = {'adverts': adverts, 'platforms': platforms}
        return render(request, 'board/main.html', context=context)


def by_platform(request, platform_name):
    adverts = Advert.objects.filter(platform__name=platform_name)
    platforms = Platform.objects.all()
    context = {'adverts': adverts, 'platforms': platforms}
    return render(request, 'board/main.html', context)


def add_and_save(request):
    if request.method == 'POST':
        adv_form = AdvertForm(request.POST)
        if adv_form.is_valid():
            adv_form.save()
            return HttpResponseRedirect(
                reverse(
                    'board:by_platform',
                    kwargs={
                        'platform_id': adv_form.changed_data['platform'].pk
                    }
                )
            )
        else:
            context = {'form': adv_form}
            return render(request, 'board/add_advert.html', context=context)
    else:
        adv_form = AdvertForm()
        return render(request, 'board/add_advert.html', context={'form': adv_form})
