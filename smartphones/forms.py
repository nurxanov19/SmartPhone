from django import forms
from django.forms import Textarea

from .models import SmartPhone


class PhoneForm(forms.ModelForm):   # forms.ModelForm berilmasa .save() ishlamaydi. Chunki, PhoneForm klassi ModelForm ning instance sifatida yaratilishi kerak
    class Meta:
        model = SmartPhone
        fields = '__all__'


    def clean_year(self):
        year = self.cleaned_data['year']
        if isinstance(year, int) and year < 2015:
            raise forms.ValidationError('We do not accept older phones')

        return year

    def clean_brand(self):
        brand = self.cleaned_data['brand']
        if brand in ['Redmi', 'SonyErikson', 'Lenovo']:
            raise forms.ValidationError(f'We do not accept {brand}')
        return brand


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data['name']

        if not name == name.capitalize():
            raise forms.ValidationError(f'Name should start with uppercase')
        return name

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) < 5:
            raise forms.ValidationError('Phone number must be bigger than 5')
        return phone