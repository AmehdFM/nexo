from django.shortcuts import render

# Create your views here.

def home(request):

    context = {
        'active_page': 'home',
    }
    return render(request, 'main/index.html', context)

