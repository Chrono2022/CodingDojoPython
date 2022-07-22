class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 1000
        self.energy = 1000

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy +=5
        self.health += 10
        print(f"{self.name} is getting fatter!")
        return self

    def play(self):
        self.health += 5
        print(f"{self.name} is at {self.health} health points!")
        return self
    def noise(self):
        print("Meow!")

Lumine = Pet("Lumine", "Cat", "Destroys Curtains")


class HyperPet(Pet):
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 1000
        self.energy = 1000

    def sleep(self):
        super().sleep()
        print("No sleep! Meow all night!")

    def eat(self):
        super().eat()
        print("Foolish mortal, I have already eaten everything! I demand more!")

    def play(self):
        super().play()
        print("ZooooooooOOOOOOOoooooooom - Sound Barrier has been broken")

    def noise(self):
        super().noise()
        print("(You know that really loud sound an animal makes? That * 1000")

Lumine_when_I_try_to_study = HyperPet("Hyper Lumine", "Hyper Cat", "Destroys all")