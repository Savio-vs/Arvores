import random
class No_arvore:
    def __init__(self,data,dad) -> None:
        self.data = data
        self.dad = dad
        self.right = None
        self.left = None

class ramo:
    def __init__(self) :
        self.boof = None
    def valor(self):
        item = self.boof 
        return item.data

    def imprimir (self):
        item = self.boof
        if item.left != None:
            esquerda = item.left
            esquerda.imprimir()
            print("fim da chamada anterior",item.data)
            if item.right != None:
                direita = item.right
                direita.imprimir()
        else:
            print("menor falor até agora",item.data)
            if item.right != None:
                proximo = item.right
                proximo.imprimir()
    
    def select_data(self,dado):
        item = self.boof    
        if item.data > dado:
            item = item.left
            item.select_data(dado)
        elif item.data < dado:
            item = item.right
            item.select_data(dado)
        else:
            print(item.data)
            
    def valor_posterior(self,dado):
        pass

#ok
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
        branch.boof = No_arvore(index,dad)
        
        
        
    
arvore1 = ramo()
#valor = [24,5,10,2,11,3,17,1,7,4,6,15]
for i in range (12):
    #valor = random.randint(1,25)
    criar(arvore1,valor[i],None)

arvore1.imprimir()