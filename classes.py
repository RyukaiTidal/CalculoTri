class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self, base,altura):
        self.base = base
        self.altura = altura
    def calculaArea(self):
        self.area = self.base*self.altura
        return self.area


    def calculaPerimetro(self):
        self.perimetro = (self.base*2)+(self.altura*2)
        return self.perimetro

class Triangulo(Forma):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def calculaArea(self):
        self.area = (self.base*self.altura)
        return self.area


    def calculaPerimetro(self,):
        self.perimetro = self.base*3
        return self.perimetro
