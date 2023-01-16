from django import forms
from .widgets import CustomClearableFileInput
from .models import Coins, Metal


class CoinsForm(forms.ModelForm):

    class Meta:
        model = Coins
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        metals = Metal.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in metals]

        self.fields['metal'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-1'
