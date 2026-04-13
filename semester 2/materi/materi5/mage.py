from hero import Hero
from monster import Monster

# panggil parent class sebagai parameter
# child class = mewarisi semua attr & method dari parent
class Mage(Hero):
    def __init__(self, name: str, hp: int):
        # super() = mengakses method dari parent class
        super().__init__(name, hp, job="Mage")

    # method baru khusus mage
    def cast_spell(self):
        print(f"{self.name} cast spell magic attack...")
    
    # timpa ultimate skill
    def ultimate(self, enemy: Monster):
        dmg = 100
        print(f"{self.name} menggunakan ultimate skill: ATOMIC BOMB! | {dmg} DMG")
        # monster kena damage
        enemy.take_damage(dmg)