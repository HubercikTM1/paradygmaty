# Abstrakcja. Enkapsulacja. Dziedziczenie. Polimorfizm.

from abc import ABC, abstractmethod

class animal(ABC):
    def __init__(self, breed, speed, color):
        # enkapsulacja
        self._breed = breed
        self._speed = speed
        self._color = color
    
    @property
    def breed(self):
        return self._breed
    @property
    def speed(self):
        return self._speed
    @property
    def color(self):
        return self._color

    # abstrakcja
    @abstractmethod
    # polimorfizm
    def speak(self):
        # pass
        print(1)

    def desc(self):
        print(f"mój gatunek to {self.breed}!")
# dziedziczenie
class cat(animal):
    def scratch(self):
        print("drapu drapu")
    # polimorfizm
    def speak(self):
        print("miau")
    def run(self):
        print(f"biegne {self.speed} km/h! jestem prendkościom!")
class dog(animal):
    def hunt(self):
        print("dogonię cie")
    # polimorfizm
    def speak(self):
        print("hau")
    def rainbow(self):
        print(f"mój kolor to {self.color}")

if __name__ == "__main__":
    pies = dog("chow chow",30,"brown")
    kot = cat("brytyjski", 35, "blue")
    # zwierze = animal("coś",69,"black")
    pies.hunt()
    pies.speak()
    pies.rainbow()
    kot.scratch()
    kot.speak()
    kot.run()
    # zwierze.desc()