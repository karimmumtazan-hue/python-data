
from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponse
from django.utils.html import escape

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def dictfetchone(cursor):
    """Mengubah satu hasil query menjadi dictionary."""
    columns = [col[0] for col in cursor.description]
    row = cursor.fetchone()

    if row is None:
        return None

    return dict(zip(columns, row))


def siswa_list(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, nama, umur, tanggal_lahir, status_hadir, nilai_akhir
            FROM siswa
            ORDER BY id DESC
        """)
        data_siswa = dictfetchall(cursor)

    search_text="bandung"

    return render(request, 'list.html', {
        'keyword': search_text,
        'data': data_siswa
    })


def siswa_detail(request, id):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM siswa
            WHERE id = %s
            """,
            [id]
        )
        siswa = dictfetchone(cursor)    

    
def siswa_create(request):
    # cek request yg masuk, klo dia POST (submit)
    if request.method == 'POST':        
        # kumpulkan data dari request post
        nama = request.POST.get('nama', '').strip()
        umur = request.POST.get('umur', '').strip()
        tanggal_lahir = request.POST.get('tanggal_lahir', '').strip()
        status_hadir = request.POST.get('status_hadir', '').strip() == 'hadir'
        nilai_akhir = request.POST.get('nilai_akhir', '').strip()

        # eksekusi query insert ke tabel siswa
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO siswa (nama, umur, tanggal_lahir, status_hadir, nilai_akhir)
                VALUES (%s, %s, %s, %s, %s)
                """,
                [nama, umur, tanggal_lahir, status_hadir, nilai_akhir]
            )

        # klo berhasil maka redirect ke siswa list
        return redirect('siswa_list')

    # klo gk submit (GET)
    return render(request, 'form.html')


def siswa_update(request, id):
    # Ambil data siswa dulu
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT id, nama, umur, tanggal_lahir, status_hadir, nilai_akhir 
            FROM siswa 
            WHERE id = %s
            """,
            [id]
        )
        siswa = dictfetchone(cursor)

    if not siswa:
        return HttpResponse("Data siswa tidak ditemukan", status=404)

    # ngumpulin data-data dulu
    if request.method == 'POST':        
        nama = request.POST.get('nama', '').strip()
        umur = request.POST.get('umur', '').strip()
        tanggal_lahir = request.POST.get('tanggal_lahir', '').strip()
        status_hadir = request.POST.get('status_hadir', '').strip() == 'hadir'
        nilai_akhir = request.POST.get('nilai_akhir', '').strip()

        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE siswa 
                SET nama = %s, umur = %s, tanggal_lahir = %s, status_hadir = %s, nilai_akhir = %s
                WHERE id = %s
                """,
                [nama, umur, tanggal_lahir, status_hadir, nilai_akhir, id]
            )
        # redirect ke siswa_list kalo berhasil
        return redirect('siswa_list')

    if siswa['tanggal_lahir']:
        try:
            siswa['tanggal_lahir'] = siswa['tanggal_lahir'].strftime('%Y-%m-%d')
        except AttributeError:
            pass

        return render(request, 'form.html', {
        'siswa': siswa,
        'is_update': True 
        })

def siswa_delete(request, id):
    # ambil data untuk konfirmasi penghapusan
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT id, nama, umur, tanggal_lahir 
            FROM siswa 
            WHERE id = %s
            """,
            [id]
        )
        siswa = dictfetchone(cursor)

    # kalo datanya gak ada
    if not siswa:
        return HttpResponse("Data siswa tidak ditemukan", status=404)

    # Proses kalo tombol "Ya, Hapus" diklik
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM siswa 
                WHERE id = %s
                """,
                [id]
            )
        # balik ke list klo dh bisa
        return redirect('siswa_list')

    # ke hlmn konfirm
    return render(request, 'delete.html', {
        'siswa': siswa
    })
