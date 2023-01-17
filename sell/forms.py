from django import forms
from .models import Sell


class SellForm(forms.ModelForm):

    class Meta:
        model = Sell
        fields = '__all__'

    image = forms.ImageField(label='Image', required=True)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'E-mail',
            'coin_name': 'Coin name',
            'description': 'Description',
            'metal': 'Metal',
            'origin': 'Origin',
            'condition': 'Condition',
            'ask_price': 'Ask price $',
            'negotiable': 'Negotiable',
            'image': 'Image',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'rounded-1 input-flds'
            if field != 'negotiable':
                self.fields[field].label = False
            else:
                self.fields[field].widget.attrs['class'] = 'mt-0'
