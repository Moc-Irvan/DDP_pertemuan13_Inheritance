from Animal import Animal

# buat minimal 3 class child (Amphibi,  Mamalia, Carnivora, dll) setiap class child itu 
class Omnivora(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, bernafas, Keunggulunnya):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.bernafas = bernafas
        self.Keunggulunnya = Keunggulunnya

    # memiliki 2 properti dan method  
    def info_animal(self):
        super().info_animal()
        print("bernafas \t\t\t : ", self.bernafas, 
              "\nKeunggulunnya \t\t\t : ", self.Keunggulunnya)

print("Objek 3 : Omnivora")
print('=============================')
hewan = Omnivora("Monyet ", "Pemakan segalanya", "darat", "melahirkan", "paru-paru", "Bisa bergelantungan")
hewan.info_animal()

print('=============================')
hewan = Omnivora("Paus ", "Pemakan segalanya", "Laut", "melahirkan", "paru-paru", "Bisa Menyeburkan Air Dibagian atasnya")
hewan.info_animal()

print('=============================')
hewan = Omnivora("Ayam ", "Pemakan segalanya", "darat", "Bertelur", "paru-paru", "Bisa berkokok")
hewan.info_animal()