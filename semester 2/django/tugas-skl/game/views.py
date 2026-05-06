from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def biodata(request):
    return render(request, 'biodata.html')

def galeri(request):
    # html_content = "<h1>🎮 Mobile Legend</h1>";
    # return HttpResponse(html_content)
    # hubungkan dengan templates file
    return render(request, 'galeri.html')

def jadwal(request):
    # hubungkan dengan templates file
    return render(request, 'jadwal.html')

def feedback(request):
    # hubungkan dengan templates file
    return render(request, 'feedback.html')