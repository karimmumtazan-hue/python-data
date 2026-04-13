from colorama import  Fore, Back, Style, init

# auto reset warna (biar gak bocor kebawah)
init(autoreset=True) 
# Class untuk nyimpen data rekening
class Rekening:
    # __init__ = constructor, otomatis jalanin object pas udah dibuat
    def __init__(self, nama, nis, saldo_awal, pin):
        self.nama = nama          # atribut biasa (bisa diakses dari luar)
        self.nis = nis
        self.__saldo = saldo_awal # double underscore = private (enkapsulasi) = biar gak bisa di otak-atik yang bukan admin
        self.__pin = pin          # PIN juga dibuat private

    # @property dipakai biar saldonya bisa dibaca seperti atribut,
    # tapi tetap tidak bisa diubah langsung dari luar class
    @property
    def saldo(self):
        return self.__saldo

    # Method setor uang
    def setor(self, jumlah):
        # validasi supaya tidak bisa setor 0 atau negatif
        if jumlah <= 0:
            print(Fore.LIGHTRED_EX + "Nominal tidak valid.")
            return  # menghentikan method lebih awal

        self.__saldo += jumlah  # menambahkan saldo
        print(Fore.GREEN + Back.LIGHTGREEN_EX + "Setor berhasil.")
        print(Fore.GREEN + Back.LIGHTGREEN_EX + "Saldo sekarang:", self.__saldo)

    # Method buat narik uang
    def tarik(self, jumlah):
        if jumlah <= 0:
            print(Fore.LIGHTRED_EX + "Nominal tidak valid.")
            return

        # cek saldo cukup atau gak
        if jumlah > self.__saldo:
            print(Fore.LIGHTRED_EX + "Saldo tidak cukup.")
            return

        self.__saldo -= jumlah  # mengurangi saldo
        print(Fore.GREEN + Back.LIGHTGREEN_EX + "Penarikan berhasil.")
        print(Fore.GREEN + Back.LIGHTGREEN_EX + "Sisa saldo:", self.__saldo)

    # Method untuk ngecek PIN saat login
    def cek_pin(self, pin):
        return pin == self.__pin  # akan menghasilkan True atau False = alurnya nanti ke menu