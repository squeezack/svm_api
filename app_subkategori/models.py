from django.db import models
from app_kategori.models import Kategori

class Subkategori(models.Model):
    id_subkategori = models.AutoField(primary_key=True)
    id_kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    nama_subkategori = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_subkategori
