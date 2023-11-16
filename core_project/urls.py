from django.urls import path
from django.contrib import admin
from app_dashboard import views as dashboard
from app_scraping import views as scraping
from app_kategori import views as kategori
from app_subkategori import views as subkategori

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", dashboard.index, name="dashboard"),
    path("scraping", scraping.index, name="scraping"),
    path("proses_id", scraping.proses_id, name="proses_id"),
    path("export_to_csv/", scraping.export_to_csv, name="export_to_csv"),
    path("kategori", kategori.index, name="kategori"),
    path("add_kategori", kategori.add, name="add_kategori"),
    path("ubah_kategori/<int:id_kategori>/", kategori.ubah_kategori, name="ubah_kategori"),
    path("hapus_kategori/<int:id_kategori>/", kategori.hapus_kategori, name="hapus_kategori"),
    path("subkategori", subkategori.index, name="subkategori"),
    path("add_subkategori", subkategori.add, name="add_subkategori"),
    path("ubah_subkategori/<int:id_subkategori>/", subkategori.ubah_subkategori, name="ubah_subkategori"),
    path("hapus_subkategori/<int:id_subkategori>/", subkategori.hapus_subkategori, name="hapus_subkategori"),
]
