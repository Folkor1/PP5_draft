from django import forms
from .models import Coins, Metal


class CoinsForm(forms.ModelForm):

    class Meta:
        model = Coins
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        metal = Metal.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in metal]
        placeholders = {
            'metal': 'Metal',
            'sku': 'SKU',
            'name': 'Name',
            'description': 'Description',
            'price': 'Price $',
            'quantity': 'Quantity',
            'origin': 'Origin',
            'year': 'Year',
            'condition': 'Condition',
            'era': 'Era',
            'image_url': 'Image URL',
            'image': 'Imagem',
        }
        self.fields['metal'].choices = friendly_names
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'rounded-1 input-flds'
            self.fields[field].label = False
