from django import forms

from pcf.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'subscription')

