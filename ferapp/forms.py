from django import forms
from .models import Image

class UploadFileForm(forms.Form):
    file = forms.FileField()

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)