class ListaException(Exception):
    def __init__(self, mensagem: object) -> None:
        super().__init__(mensagem)

class Lista:
    def __init__(self):
        self.__dados = []
    #verifica se a pilha está vazia
    def estaVazia(self):
        return len(self.__dados) == 0
    #retorna o tamanho da pilha
    def tamanho(self):
        return len(self.__dados)
    #informa o conteúdo em determinada posição
    def elemento(self,posicao):
        return self.__dados[posicao]
    #retorna a posição do conteúdo determinado
    def busca(self,conteudo):
        return self.__dados.index[conteudo]
    #modifica um valor em determinada posição
    def modificar(self,posicao,conteudo):
        return self.__dados.insert(posicao,conteudo)
    #empihlar elementos na pilha
    def empilhar(self,posicao,elemento):
        return self.__dados.insert(posicao,elemento)
    #remove elementos do topo da pilha, caso ela está com elemento
    def desempilhar(self,posicao):
        if self.estaVazia():
            raise ListaException('Pilha Vazia, impossível desempilhar!')
        return self.__dados.pop(posicao)
    #Método para esvazia a pilha. indepentende da linguagem de programação. OBS: precisa existe o metodo desempilhar
   

    def esvazia(self):
        while(not self.estaVazia()):
            self.desempilhar()
    #imprime a pilha
    '''def __str__(self):
       print (self.__dados.__str__())'''

    def __str__(self) -> str:
        s = '[ '
        for e in self.__dados:
            s += f'{e} '
        return f'{s} ] <- topo'

    def clone(self):
        copy = Lista()
        for i in range(self.tamanho()):
            copy.empilhar(self.elemento(i))
        return copy

    def concat(self,outraPilha):
        aux = Lista()
        while(not outraPilha.estaVazia()):
            aux.empilhar(outraPilha.desempilhar())
        while(not aux.estaVazia()):
            self.empilhar(aux.desempilhar())

    def inverte(self):
        pilhaAux = Lista()
        secudaria = Lista()
        while(not self.estaVazia()):
            pilhaAux.empilhar(self.desempilhar())
        while(not pilhaAux.estaVazia()):
            secudaria.empilhar(pilhaAux.desempilhar())
        while(not secudaria.estaVazia()):
            self.empilhar(secudaria.desempilhar())
       
    def inverte2(self):
        aux = Lista()
        while(not self.estaVazia()):
            aux.empilhar(self.desempilhar())
        self.__dados = aux.__dados
        return self.__dados

    def clone2 (self):
        aux = Lista()
        for i in self.__dados:
            aux.empilhar(i)
        return aux
     
     
     
      #while(not aux.estaVazia()):
            #self.empilhar(aux.desempilhar()) 




        
        
        
