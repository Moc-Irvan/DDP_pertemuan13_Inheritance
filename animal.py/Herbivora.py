from Animal import Animal

# buat minimal 3 class child (Amphibi,  Mamalia, Carnivora, dll) setiap class child itu 
class Herbivora(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, secara_berkelompok, habitat):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.secara_berkelompok = secara_berkelompok
        self.habitat = habitat

    # memiliki 2 properti dan method  
    def info_animal(self):
        super().info_animal()
        print("Secara Berkelompok \t\t : ", self.secara_berkelompok, 
              "\nHabitat \t\t\t : ", self.habitat)

print("Objek 2 : Herbivora")
print('=============================')
hewan = Herbivora("Gajah", "Buah", "darat", "Melahirkan", "Ya", "hutan")
hewan.info_animal()

print('=============================')
hewan = Herbivora("Burung", "Buah dan biji-bijian", "udara", "Bertelur", "Ya", "hutan")
hewan.info_animal()

print('=============================')
hewan = Herbivora("Zebra", "Buah, rumput, dan tumbuhan lainnya", "darat", "Melahirkan", "Ya", "hutan")
hewan.info_animal()