from django.shortcuts import render

# Create your views here.
def index (request):
    context = {
        'title' : "ini adalah halaman dashboard "
    }
    return render(request, 'pages/dashboard/index.html', context)
