from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'active_page': 'recursos',
    }
    return render(request, 'recursos/index.html', context)