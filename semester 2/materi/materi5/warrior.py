from hero import Hero
from monster import Monster

class Warrior(Hero):
    def __init__(self, name: str, hp: int):
        # super() = mengakses method dari parent class
        super().__init__(name, hp, job="Warrior")

    # timpa ultimate skill
    def ultimate(self, enemy: Monster):
        dmg = 125
        print(f"{self.name} menggunakan ultimate skill: EXCALIBUR! | {dmg} DMG")
        # monster kena damage
        enemy.take_damage(dmg)
        