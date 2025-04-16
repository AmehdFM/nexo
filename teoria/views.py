from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'active_page': 'teoria',
    }
    return render(request, 'teoria/index.html', context)