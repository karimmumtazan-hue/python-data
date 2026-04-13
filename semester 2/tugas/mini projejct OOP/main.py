from colorama import  Fore, Back, Style, init
from rekening import Rekening
# auto reset warna (biar gak bocor kebawah)
init(autoreset=True) 

# Class utama untuk sistem ATM
class BankSystem:
    def __init__(self):
        # dictionary dipakai sebagai database sederhana
        # key = NIS, value = object Rekening
        self.data_rekening = {}

    # Method utama program
    def jalan(self):
        print(Back.LIGHTBLUE_EX + Fore.BLUE + "Program ATM Sederhana")

        # while True = loop terus sampai user ketik exit
        while True:
            nis = input(Fore.BLUE + "\nMasukkan NIS (6 digit) atau exit: ")

            # keluar dari program
            if nis.lower() == "exit":  # lower() supaya tidak case sensitive
                print(Fore.GREEN + Back.LIGHTGREEN_EX +"Program selesai.")
                break  # keluar dari loop

            # validasi NIS harus angka dan panjangnya 6
            if not nis.isdigit() or len(nis) != 6:
                print(Fore.LIGHTRED_EX + "NIS harus 6 angka.")
                continue  # kembali ke awal loop

            # cek apakah NIS sudah ada di dictionary
            if nis in self.data_rekening:
                akun = self.data_rekening[nis]  # ambil object rekening

                kesempatan = 3  # batas percobaan PIN

                # loop percobaan PIN
                while kesempatan > 0:
                    pin = input(Fore.BLUE + "Masukkan PIN: ")

                    if akun.cek_pin(pin):
                        self.menu(akun)  # masuk ke menu jika benar
                        break
                    else:
                        kesempatan -= 1
                        print(Fore.LIGHTRED_EX + "PIN salah. Sisa:", kesempatan)

                # kalau kesempatan habis
                if kesempatan == 0:
                    print(Fore.LIGHTRED_EX + "Akun dikunci sementara.")

            else:
                print(Fore.RED + "NIS belum terdaftar.")
                self.buat_rekening(nis)

    # Method untuk membuat rekening baru
    def buat_rekening(self, nis):
        print(Fore.GREEN + Back.LIGHTGREEN_EX +"\nBuka Rekening Baru")

        # validasi nama (hanya huruf dan spasi)
        while True:
            nama = input(Fore.BLUE + "Masukkan nama: ")

            # replace(" ", "") supaya spasi tidak dihitung
            if nama.replace(" ", "").isalpha():
                break
            else:
                print(Fore.LIGHTRED_EX + "Nama hanya boleh huruf.")

        # validasi saldo awal
        while True:
            try:
                # int() bisa error kalau input bukan angka
                saldo_awal = int(input(Fore.BLUE + "Masukkan saldo awal: "))

                if saldo_awal < 0:
                    print(Fore.LIGHTRED_EX + "Saldo tidak boleh negatif.")
                    continue

                break
            except:
                # except menangkap error kalau input bukan angka
                print(Fore.LIGHTRED_EX + "Saldo harus angka.")

        # validasi PIN (harus 4 digit angka)
        while True:
            pin = input(Fore.BLUE + "Buat PIN 4 digit: ")

            if pin.isdigit() and len(pin) == 4:
                break
            else:
                print(Fore.LIGHTRED_EX + "PIN harus 4 angka.")

        # membuat object Rekening dan menyimpannya ke dictionary
        self.data_rekening[nis] = Rekening(nama, nis, saldo_awal, pin)

        print(Fore.GREEN + Back.LIGHTGREEN_EX + "Rekening berhasil dibuat.")
        # bakal agak bingung di terminalnya, jadi di kasih ini
        print(Fore.MAGENTA +"NIS-nya yang 6 digit yang pertama kamu masukkin")

    # Menu transaksi setelah login = tepatnya habis masukin pin
    def menu(self, akun):
        while True:
            print(Back.LIGHTBLUE_EX + Fore.BLUE + "     Menu      ")
            print(Fore.BLUE + "1. Setor")
            print(Fore.BLUE + "2. Tarik")
            print(Fore.BLUE + "3. Cek Saldo")
            print(Fore.BLUE + "4. Logout")

            pilih = input(Fore.BLUE + "Pilih: ")

            if pilih == "1":
                try:
                    jumlah = int(input(Fore.BLUE + "Jumlah setor: "))
                    akun.setor(jumlah)
                except:
                    # kalau user input huruf
                    print(Fore.LIGHTRED_EX + "Input harus angka.")

            elif pilih == "2":
                try:
                    jumlah = int(input(Fore.BLUE + "Jumlah tarik: "))
                    akun.tarik(jumlah)
                except:
                    print(Fore.LIGHTRED_EX + "Input harus angka.")

            elif pilih == "3":
                print(Fore.GREEN + Back.LIGHTGREEN_EX + "Saldo saat ini:", akun.saldo)

            elif pilih == "4":
                print(Back.LIGHTBLUE_EX + Fore.BLUE + "Logout berhasil.")
                break

            else:
                print(Fore.LIGHTRED_EX + "Pilihan tidak tersedia.")


# ini supaya program hanya jalan kalau file dijalankan langsung
# bukan saat di-import ke file lain
if __name__ == "__main__":
    atm = BankSystem()
    atm.jalan()
