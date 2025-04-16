from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'active_page': 'ejercicios',
    }
    return render(request, 'ejercicios/index.html', context)