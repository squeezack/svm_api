from django import forms
from .models import Kategori

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama_kategori']

    def __init__(self, *args, **kwargs):
        super(KategoriForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
