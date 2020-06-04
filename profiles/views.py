from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse

from board.models import Advert
from .models import UserProfile
from .forms import UserProfileForm


class ProfileDetailView(DetailView):
    """Page of UserProfile detail information"""
    model = UserProfile
    context_object_name = 'profile'
    template_name = 'profiles/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['adverts'] = Advert.objects.filter(
            user_id=self.kwargs.get('pk')
        )

        return context


class ProfileUpdateView(UpdateView):
    """Form to change UserProfile and User information"""
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profiles/profile_update.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.kwargs.get('pk')})
