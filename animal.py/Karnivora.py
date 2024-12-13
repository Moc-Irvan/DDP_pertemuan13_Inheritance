from Animal import Animal

# buat minimal 3 class child (Amphibi,  Mamalia, Carnivora, dll) setiap class child itu 
class Karnivora(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, Berkaki, ukuran_tubuh):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.Berkaki = Berkaki
        self.ukuran_tubuh = ukuran_tubuh

    # memiliki 2 properti dan method  
    def info_animal(self):
        super().info_animal()
        print("Berkaki \t\t\t : ", self.Berkaki, 
              "\nukuran_tubuh \t\t\t : ", self.ukuran_tubuh)

print("Objek 1 : KARNIVORA")    
print('=============================')
hewan = Karnivora("Ikan Hiu", "Ikan", "Laut", "bertelur", "Tidak memiliki kaki", "Besar")
hewan.info_animal()

print('=============================')
hewan = Karnivora("Ular", "Daging", "Laut dan darat", "bertelur", "Tidak memiliki kaki", "Besar dan kecil")
hewan.info_animal()

print('=============================')
hewan = Karnivora("Harimau", "Daging", "Darat", "Melahirkan", "Memiliki 4 kaki", "Besar")
hewan.info_animal()