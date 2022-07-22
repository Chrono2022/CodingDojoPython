from Dojo_Pets_Parent import *

class Ninja():
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    
    def walk(self):
        self.pet.play()
        print(f"Thanks for walking me! Love, {self.pet.name}")

    def feed(self):
        self.pet.eat()
        print(f"Om nom nom nom....{self.pet.name} says loudly")

    def bathe(self):
        self.pet.noise()
        print(f"Hiss! Scratch! (Perhaps {self.pet.name} doesn't like water)")

Nathan = Ninja("Nathan", "Ingersoll", Lumine, "turkey", "Purina")

Nathan.walk()
Nathan.feed()
Nathan.bathe()

Busy_Nathan = Ninja("Nathan", "Ingersoll", Lumine_when_I_try_to_study, "turkey", "Purina")

Busy_Nathan.walk()
Busy_Nathan.feed()

print(Lumine.energy)
print(Lumine_when_I_try_to_study.health)