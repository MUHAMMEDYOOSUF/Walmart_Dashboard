from django import forms

from DashWalmartApp.models import my_ml


class DataForm(forms.ModelForm):
    class Meta:
        model = my_ml
        fields = ['temp', 'fuel', 'cpi', 'unemp', 'week', 'ishol', 'store', 'dept', 'typ', 'size']
