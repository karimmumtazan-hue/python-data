from hero import Hero
from monster import Monster

class Assasin(Hero):
    def __init__(self, name: str, hp: int):
        super().__init__(name, hp, job="Assasin")

    def ultimate(self, enemy: Monster):
        dmg = 130
        print(f"{self.name} menggunakan ultimate skill: SHADOW KILL! | {dmg} DMG")
        enemy.take_damage(dmg)
        