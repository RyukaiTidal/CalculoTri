class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()
    def calculaArea(self,base,altura):
        self.area = base*altura
        print(self.area)


    def calculaPerimetro(self,base,altura):
        self.perimetro = 2*(base*altura)
        print(self.perimetro)

class Triangulo(Forma):
    def __init__(self):
        super().__init__()
    def calculaArea(self,base,altura):
        self.area = (base*altura)/2
        print(self.area)


    def calculaPerimetro(self, lado):
        self.perimetro = lado * 3
        print (self.perimetro)
