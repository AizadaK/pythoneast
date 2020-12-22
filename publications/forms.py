from django.forms import forms
from .models import Publication

class PublicationForm(ModelForm):
    # name = CharField(max_length=10, help_text='Напишите название публикации')
    # text = forms.TextInput(required=True)
    # test = forms.CharField(required=True)
    class Meta:
        model = Publication
        fields = ["name", "text", "image"]
