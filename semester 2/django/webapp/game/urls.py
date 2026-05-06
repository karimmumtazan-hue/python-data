from django.urls import path
from . import views

urlpatterns = [
    # halaman  index / yg awal
    path('', views.menu_game),
    # halaman /moba
    path('moba', views.moba),
    # halaman /genshin
    path('genshin', views.genshin),
]
