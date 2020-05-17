from django.forms import ModelForm, DecimalField
from django.forms.widgets import Select
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Advert


class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        fields = (
            'platform',
            'title',
            'content',
            'advert_category',
            'content_type',
            'price',
        )
        help_texts = {'content': 'Опишите услугу'}
        field_classes = {'price': DecimalField}
        widgets = {
            'platform': Select,
            'advert_category': Select,
            'content_type': Select,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить изменения'))
