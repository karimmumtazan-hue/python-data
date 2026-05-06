from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def menu_game(request):
    return render(request, 'portal.html')

def moba(request):
    # html_content = "<h1>🎮 Mobile Legend</h1>";
    # return HttpResponse(html_content)
    # hubungkan dengan templates file
    return render(request, 'moba.html')

def genshin(request):
    # hubungkan dengan templates file
    return render(request, 'genshin.html')

def dota(request):
    # hubungkan dengan templates file
    return render(request, 'dota.html')