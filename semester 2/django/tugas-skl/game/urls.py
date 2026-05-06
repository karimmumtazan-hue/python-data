from django.urls import path
from . import views

urlpatterns = [
    # halaman  index / yg awal
    path('', views.biodata, name='biodata'),
    # halaman /moba
    path('galeri/', views.galeri, name='galeri'),
    # halaman /genshin
    path('jadwal/', views.jadwal, name='jadwal'),
    # halaman /dota
    path('feedback/', views.feedback, name='feedback'),
]
