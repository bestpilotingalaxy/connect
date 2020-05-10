from django.forms import ModelForm, DecimalField
from django.forms.widgets import Select

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
