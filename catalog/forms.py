from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        word_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in word_list:
            if word in cleaned_data:
                raise forms.ValidationError(f'использование слова "{word}" недопустимо')
        return cleaned_data
