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
            print(item.data)
            if item.right != None:
                direita = item.right
                direita.imprimir()
        else:
            print(item.data)
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
            
#ok
def div_lista (branch,lista):
    tamanho = len(lista)
    if tamanho > 1:
        meio = int(tamanho / 2)
        print(lista[meio])
        criar (branch, lista[meio], None)
 
        print (lista[ : meio])
        div_lista (branch , lista[ : meio])
        
        print(lista[meio : ] )
        div_lista (branch,lista[meio : ])
    else:
        criar (branch, lista[0] ,None)
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
        branch.boof = No_arvore(index,dad)
        
#inicio da execução
arvore1 = ramo()
valor = [1,2,3,4,5,6,7,8,9,10,11,12]
div_lista(arvore1, valor )

arvore1.imprimir()