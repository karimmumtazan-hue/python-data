from colorama import Fore, Back, Style, init
from monster import Monster
from mage import Mage
from warrior import Warrior
from archer import Archer
from assasin import Assasin

# auto reset warna (biar gak bocor kebawah)
init(autoreset=True) 
# Fore = Foreground = Warna Teks
# Back = Background = Warna Latar Belakang Teks
print(Fore.YELLOW + Back.GREEN + "=== GAME START ===")
# Style = Ganti style teks (BRIGHT, DIM, NORMAL, RESET_ALL)
print(Style.BRIGHT + Fore.RED + "=== MANYALA BOSQUE ===")

aldos = Warrior("Aldos", 100)
nana = Mage("Nana", 100)
hanabi = Archer("Archer", 100)
hanzo = Assasin("Assasin", 100)
dragon = Monster("Dragon King", 1000)

# setter via @property
aldos.hp = 250
nana.hp = 150
# update attr hp
# nana.set_hp(50)
# aldos.set_hp(100)

# ambil attr hp via @property
print(f"HP Nana: {nana.hp}")
print(f"HP Aldos: {aldos.hp}")
# print(aldos)
# print(nana)
# print(dragon)

# nana.heal()
# nana.cast_spell()
# nana.ultimate(dragon)
# aldos.ultimate(dragon)

print("=== ⚔️ RAID PARTY DI MULAI! ⚔️ ===")
# list hero di party
list_party = [aldos, nana, hanabi, hanzo]

running = True 
# loop/ulangi sampai status running jdi false
while running: 
    print("=" * 32)
    print(dragon)
    print("=== 🛡️ PILIHAN AKSI: ")
    print("*** 1. ⚔️  ATTACK")
    print("*** 2. 🧪 HEAL")
    print("*** 3. 🔥 ULTIMATE")
    print("*** 4. 🏆 EXIT")
    print("=" * 32)
    # cek aksi harus angka 1-4 saja 
    aksi = 0 
    try:
        aksi = int(input("=== 🏹 AKSI MU : "))
    except ValueError:
        print("⚠️ Inputan salah, harus angka!")

    # eksekusi berdasarkan no aksi
    if (aksi == 1):
        # aldos.attack(dragon, 10)
        # nana.attack(dragon, 10)
        # hanabi.attack(dragon, 10)
        # hanzo.attack(dragon, 10)
        # == cara diatas tdk efisien ==
        # set static dmg 10 aja dlu
        atkDmg = 10
        # gunakan looping dari list party
        for party in list_party:
            party.attack(dragon, atkDmg)
        
        # cek jika hp musuh 0, akhir game
        if dragon.hp == 0:
            running = False
            print("=== 🏆 END GAME, MUSUH KALAH!! ===\n")
    elif (aksi == 4):
        running = False
        print("=== 🏆 END GAME, BYE BYE! ===\n")
    else:
        print("⚠️ Pilihan aksi salah, hanya 1-4!")
