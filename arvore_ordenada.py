import random 
class No_arvore: 
    def __init__(self,data,dad) -> None: 
        self.data = data 
        self.dad = dad 
        self.right = None 
        self.left = None

class ramo:
    def __init__(self):
        self.boof = None 
        
    def valor(self): 
        item = self.boof 
        return item.data
        
    def imprimir (self):
        item = self.boof
        if item.left != None:
            esquerda = item.left
            esquerda.imprimir()
            #print("Desviando para esquerda",item.data)
            if item.right != None:
                #print('Desviando para direita')
                direita = item.right
                direita.imprimir()
        else:
            #print("menor falor até agora",item.data)
            if item.right != None:
                proximo = item.right
                proximo.imprimir()


#ok.... Recebe números aleatorios e monta uma arvore.
def criar(branch ,index, dad):
    if branch.boof != None :
        no = branch.boof 
        if no.data > index: 
            if no.left == None: 
                no.left = ramo()
                criar(no.left , index,no)
            else:
                criar(no.left,index,no) 
        
        elif no.data < index:
            if no.right ==None:
                no.right = ramo()
                criar(no.right , index, no)
            else:
                criar(no.right,index,no)
        
        else:
            print("numero repetido.")
        
    else: 
        #print('chegou o número',index)
        branch.boof = No_arvore(index,dad)

arvore1 = ramo()

lista = [1,2,3,4,5,6,7,8,9,10]
tamanho = len(lista)

for i in range(tamanho):
    index = int(len(lista)/2)
    criar(arvore1,lista.pop(index),None)

arvore1.imprimir()