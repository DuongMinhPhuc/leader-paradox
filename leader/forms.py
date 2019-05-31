from django import forms
from .models import Member

class AddForm(forms.ModelForm):
    class Meta: #cu phap mac dinh
        model = Member
        fields = ('name','start','end',)
