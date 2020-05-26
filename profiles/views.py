from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse

from .models import UserProfile
from .forms import UserProfileForm


class ProfileDetailView(DetailView):
    model = UserProfile
    context_object_name = 'profile'
    template_name = 'profiles/profile_detail.html'


class ProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profiles/profile_update.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.kwargs.get('pk')})


