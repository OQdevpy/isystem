from django import forms
from .models import *
from django.forms import inlineformset_factory,formset_factory,modelformset_factory
class DavomatForm(forms.ModelForm):
      class Meta:
            model=Davomat
            fields ="__all__"
            
class DavomatForm(forms.ModelForm):
      class Meta:
            model=Davomat
            fields ="__all__"
            
class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()

from django.forms import formset_factory
ArticleFormSet = formset_factory(ArticleForm,extra=2)
