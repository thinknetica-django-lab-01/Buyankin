from django import forms
from .models import Seller
from django.core.exceptions import ValidationError

class UpdateProfile(forms.ModelForm):
    age=forms.IntegerField()

    def clean_age(self):
        if self.cleaned_data['age']<18:
            raise ValidationError('Возвращайтесь когда вам исполнится 18 лет')
        return self.cleaned_data['age']

    class Meta:
        model = Seller
        fields = '__all__'