from django import forms
from catalog.models import Product

# Checks the admin forms and raise validation on pricing


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('Price must be greater than 0.')
        return self.cleaned_data['price']
