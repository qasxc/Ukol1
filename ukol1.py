import math
from abc import ABC, abstractmethod

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient


class Property(ABC):
    @abstractmethod
    def calculate_tax():
        pass
        

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        self.locality = locality
        self.area = area
        self.estate_type = estate_type

    def __str__(self):
        return f"{self.estate_type} (koeficient typu pozemku {estate_type_koef[self.estate_type]}), lokalita {self.locality.name} (místní koeficient = {self.locality.locality_coefficient}), {self.area} metrů čtverečních, daň činí {self.calculate_tax()}Kč."

    def calculate_tax(self):   
        # plocha pozemku * koeficient dle typu pozemku (atribut estate_type) * místní koeficient
        tax = self.area * estate_type_koef[self.estate_type] * self.locality.locality_coefficient
        #(pro zaokrouhlení použij funkci ceil() z modulu math)
        return math.ceil(tax)
        #return tax     
    

class Residence(Property):
    def __init__(self, name, locality, area, commercial):
        self.locality = locality
        self.name = name
        self.area = area
        self.commercial = commercial

    def __str__(self):
        return f"{self.name}, lokalita {self.locality.name}, (koeficient = {self.locality.locality_coefficient}), {self.area} metrů čtverečních, daň činí {self.calculate_tax()}Kč."


    def calculate_tax(self):
        #podlahová plocha * koeficient lokality * 15
        tax = self.area * self.locality.locality_coefficient * 15
        if self.commercial == True:
            tax *= 2
        return math.ceil(tax)

estate_type_koef = {
    "Zemědělský pozemek": 0.85,
    "Stavební pozemek": 9,
    "Les":0.35,
    "Zahrada": 2,
}

manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3)

zemedelsky_pozemek = Estate(manetin, "Zemědělský pozemek", 900)  
print(zemedelsky_pozemek)

zahrada = Estate(brno, "Zahrada", 100)
print(zahrada)

dum = Residence("Dům", manetin, 120, False)
print(dum)

kancelar = Residence("Kancelář", brno, 90, True)
print(kancelar)

