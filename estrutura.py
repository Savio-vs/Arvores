import random

class No_arvore:
    def __init__(self,data) -> None:
        self.data = data
        self.right = None
        self.left = None

class arvore:
    def __init__(self) -> None:
        self.boof = None
    def valor(self):
        item = self.boof 
        return item.data

    def imprimir (self):
        valor = self.boof
        
        

#ok
def criar(branch ,index):
    if branch.boof != None :
        no = branch.boof
        if no.data > index:
            if no.left == None: 
                no.left = arvore()
                print("esquerdo->",index)
                criar(no.left , index)
            else:
                print('indo p/ esquerda com ',index)
                criar(no.left,index) 
            
        elif no.data < index:
            if no.right ==None:
                no.right = arvore()
                print("direito->",index)
                criar(no.right , index)
            else:
                print('indo p/ direita com ',index)
                criar(no.right,index)
            
        else:
            print("numero repetido.")
            
    else:
        
        branch.boof = No_arvore(index)
        print('valor guardado',branch.valor())
        
        
    
arvore1 = arvore()

for i in range (10):
    valor = random.randint(1,25)
    criar(arvore1,valor)

arvore1.imprimir()