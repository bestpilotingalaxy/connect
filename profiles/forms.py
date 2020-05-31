from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import UserProfile


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'username',
            'email',
            'avatar',
            'nickname',
            'first_name',
            'last_name',
            'about',
            'messenger',
            'contact_phone',
            'contact_link'
        )
        help_texts = {
            'contact_phone': 'Номер телефона',
            'social_link': 'Ссылка для связи с вами',
            'first_name': 'Имя',
            'last_name': 'Фамилия'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить изменения'))
