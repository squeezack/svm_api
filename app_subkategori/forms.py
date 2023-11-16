from django import forms
from .models import Subkategori
from app_subkategori.models import Kategori

class SubkategoriForm(forms.ModelForm):
    class Meta:
        model = Subkategori 
        fields = ['id_kategori', 'nama_subkategori']

    def __init__(self, *args, **kwargs):
        super(SubkategoriForm, self).__init__(*args, **kwargs)
        self.fields['id_kategori'].widget.attrs.update({'class': 'form-control'})
        self.fields['nama_subkategori'].widget.attrs.update({'class': 'form-control'})

        # Menambahkan Bootstrap select widget untuk id_kategori
        self.fields['id_kategori'].widget = forms.Select(attrs={'class': 'form-control selectpicker'})

        # Menampilkan nama_kategori di form sebagai teks yang dapat dipilih
        self.fields['id_kategori'].queryset = Kategori.objects.all()
        self.fields['id_kategori'].label_from_instance = lambda obj: f'{obj.nama_kategori}'
