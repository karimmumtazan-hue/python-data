from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def menu_game(request):
    html_content = """<!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <title>Nexus Game Portal - Lobi Utama</title>
        <style>
            body {
                background-color: #222222;
                color: #ffffff;
                font-family: Arial, sans-serif;
                padding: 30px;
            }
            a {
                color: #4CAF50;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <h1>🕹️ Nexus Game Hub 🕹️</h1>
        <hr>
        <p>Selamat datang di lobi utama! Silakan pilih menu di bawah ini untuk menguji Routing URL Anda:</p>
        
        <ul>
            <li>
                <h2><a href="/game/moba">⚔️ Mobile Legends</a></h2>
                <p>Pilih role hero terbaikmu dan pelajari tugasnya di Land of Dawn.</p>
            </li>
            <br>
            <li>
                <h2><a href="/game/genshin">✨ Genshin Impact</a></h2>
                <p>Eksplorasi 7 elemen Teyvat dan pelajari reaksi elemental-nya.</p>
            </li>
        </ul>
    </body>
    </html>"""

    return HttpResponse(html_content)

def moba(request):
    # html_content = "<h1>🎮 Mobile Legend</h1>";
    # return HttpResponse(html_content)
    # hubungkan dengan templates file
    return render(request, 'moba.html')

def genshin(request):
    # hubungkan dengan templates file
    return render(request, 'genshin.html')