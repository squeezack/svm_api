from django.shortcuts import render, get_object_or_404, redirect
from .models import Kategori
from .forms import KategoriForm

def index(request):
    kategoris = Kategori.objects.all()
    return render(request, 'pages/kategori/index.html', {'kategoris': kategoris})

def add(request):
    if request.method == 'POST':
        form = KategoriForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kategori')
    else:
        form = KategoriForm()
    return render(request, 'pages/kategori/add.html', {'form': form})

def ubah_kategori(request, id_kategori):
    kategori = get_object_or_404(Kategori, id_kategori=id_kategori)

    if request.method == 'POST':
        form = KategoriForm(request.POST, instance=kategori)
        if form.is_valid():
            form.save()
            return redirect('kategori') 
    else:
        form = KategoriForm(instance=kategori)

    return render(request, 'pages/kategori/edit.html', {'form': form, 'kategori': kategori})

def hapus_kategori(request, id_kategori):
    kategori = get_object_or_404(Kategori, id_kategori=id_kategori)
    kategori.delete()
    return redirect('kategori')
