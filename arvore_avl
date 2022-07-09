
class No_arvore:
    def __init__(self,data,dad,piso) -> None:
        self.data = data
        self.dad = dad
        self.andar = piso
        self.right = None
        self.left = None

class ramo:
    def __init__(self) :
        self.boof = None

    def imprimir (self):#imprimi a arvore em ordem crescente.
        item = self.boof
        if item.left != None:
            esquerda = item.left
            esquerda.imprimir()
            print(item.data , 'no piso', item.andar)
            if item.right != None:
                direita = item.right
                direita.imprimir()
        else:
            print(item.data , 'no piso', item.andar)
            if item.right != None:
                proximo = item.right
                proximo.imprimir()


# adiciona um numero a arvore.
def criar(branch ,index, dad ,piso):
    if branch.boof != None :
        no = branch.boof
        if no.data > index:
            if no.left == None: 
                no.left = ramo()
                if no.right != None: 
                    item = no.right
                    item = item.boof
                    criar(no.left , index, no, item.andar)
                    
                else:
                    criar(no.left , index, no, no.andar)
                    filho = no.left
                    filho = filho.boof
                    if filho.andar == no.andar:
                        no.andar += 1
            else:
                criar(no.left, index, no , None) 
                filho = no.left
                filho = filho.boof
                if filho.andar == no.andar:
                    no.andar += 1
                if no.right != None and no.dad != None:
                    direito = no.right
                    direito = direito.boof
                    direito.andar += 1
            
        elif no.data < index:
            if no.right == None:
                no.right = ramo()
                if no.left != None :
                    item = no.left
                    item = item.boof
                    criar(no.right , index, no, item.andar)
                    
                else:
                    criar(no.right , index, no, no.andar)
                    filho = no.right
                    filho = filho.boof
                    if filho.andar == no.andar:
                        no.andar += 1
            else:
                criar(no.right,index,no, None)
                filho = no.right
                filho = filho.boof
                if filho.andar == no.andar:
                    no.andar += 1
                if no.left != None and no.dad != None:
                    esquerdo = no.left
                    esquerdo = esquerdo.boof
                    esquerdo.andar += 1
            
        else:
            print("numero repetido.")

    else: 
        branch.boof = No_arvore(index,dad,piso)

def fator_balanceamento(esquerda, direita):
    fator = esquerda - direita
    return fator
          
def maior(esquerdo,direito):
    if esquerdo == None and direito==None:
        return 0
    if esquerdo != None:
        altura_e = esquerdo.boof
        altura_e = altura_e.andar
    else:
        altura_d = direito.boof
        altura_d = altura_d.andar
        return altura_d
    
    if direito != None:
        altura_d = direito.boof
        altura_d = altura_d.andar
    else:
        return altura_e

    if altura_e > altura_d:
        return altura_e
    else:
        return altura_d

def rot_esquerda(branch):
    raiz = branch.boof
    esquerdo = raiz.right
    esquerdo = esquerdo.boof
    if esquerdo.left != None:
        f = esquerdo.left
        raiz.right = f
    else:
        raiz.right = None
    esquerdo.left = branch
    #print(raiz.left,'\n',raiz.right)
    raiz.andar = maior(raiz.left,raiz.right) +1
    esquerdo.andar = maior(esquerdo.left,esquerdo.right) +1    
    #print(esquerdo.andar,'\n',esquerdo)
    return esquerdo

def rot_direita(raiz):
    direito = raiz.left
    direito = direito.boof
    if direito.right != None:
        f = direito.right
        raiz.left = f
    direito.right = raiz
    raiz.andar = maior(raiz.left,raiz.right) +1
    direito.andar = maior(direito.left,direito.right) + 1
    return direito

def balanceamento(branch):
    andar = branch.boof
    if andar.right != None:
        direita = andar.right
        direita = direita.boof
        direita = direita.andar
    else:
        direita = 0
    if andar.left != None:
        esquerda = andar.left
        esquerda = esquerda.boof
        esquerda = esquerda.andar
    else:
        esquerda = 0

    fator = fator_balanceamento(esquerda,direita)
    print(fator)
    if fator >=2:
        pass
    elif fator <= -2:
        branch.boof = rot_esquerda(branch)
        teste = branch.boof
        
        print(teste.data, '\n',teste.andar,'\n',teste.left)
       
    else:
        print('pegamos andares errados!')
    
