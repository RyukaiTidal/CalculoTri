from classes import *

tri = Triangulo(4,3)
ret = Retangulo(6,10)

atri = tri.calculaArea()
ptri = tri.calculaPerimetro()
aret = ret.calculaPerimetro()
pret = ret.calculaArea()


print(atri, ptri, aret, pret)