from arvore_avl import *

avr = ramo()
valores = [10,25,35]
#enviar cada item da lista de valores para uma arvore
for i in valores:
    criar (avr,i,None,1)

balanceamento(avr)
