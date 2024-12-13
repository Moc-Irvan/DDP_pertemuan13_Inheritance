# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti 
# (name, makanan, hidup, berkembang biak)

class Animal :
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    
    def info_animal(self):
        print("Nama Hewan \t\t\t : ", self.name,
              "\nMakanan \t\t\t : ", self.makanan,
              "\nhidup \t\t\t\t : ", self.hidup,
              "\nberkembang_biak \t\t : ", self.berkembang_biak,)



