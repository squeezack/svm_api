from django.shortcuts import render, get_object_or_404, redirect
from .models import Subkategori
from .forms import SubkategoriForm

def index(request):
    subkategoris = Subkategori.objects.all()
    return render(request, 'pages/subkategori/index.html', {'subkategoris': subkategoris})

def add(request):
    if request.method == 'POST':
        form = SubkategoriForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subkategori')
    else:
        form = SubkategoriForm()
    return render(request, 'pages/subkategori/add.html', {'form': form})

def ubah_subkategori(request, id_subkategori):
    subkategori = get_object_or_404(Subkategori, id_subkategori=id_subkategori)

    if request.method == 'POST':
        form = SubkategoriForm(request.POST, instance=subkategori)
        if form.is_valid():
            form.save()
            return redirect('subkategori') 
    else:
        form = SubkategoriForm(instance=subkategori)

    return render(request, 'pages/subkategori/edit.html', {'form': form, 'subkategori': subkategori})

def hapus_subkategori(request, id_subkategori):
    subkategori = get_object_or_404(Subkategori, id_subkategori=id_subkategori)
    subkategori.delete()
    return redirect('subkategori')
