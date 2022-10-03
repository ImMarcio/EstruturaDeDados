class FilaException(Exception):
    def __init__(self, mensagem) :
        super().__init__(mensagem)



class FilaSequencial:
    def __init__(self) :
        self.__dados = []
    #método para verificar se a fila está vazia
    def estaVazia(self)-> bool:
        return len(self.__dados) == 0
    #método para saber o tamanho da fila
    def tamanho(self):
        return len(self.__dados)
    def inicio(self):
        if self.estaVazia():
            raise FilaException('A Fila está vazia')
        return self.__dados[0]
    #método para inserir elementos na fila  na última posição
    def inserir (self,dado):
        self.__dados.append(dado)
    #método para remover elemento da fila na posição 0
    def remover (self):
        if self.estaVazia():
            raise FilaException('A Fila está vazia')        
        return self.__dados.pop(0)

    def __str__(self):
        return self.__dados.__str__()
    
    def imprimir(self):
        print(self.__str__())


if __name__ == '__main__':
    f = FilaSequencial()
    try:
        f.remover()
    except FilaException as fe:
        print(fe)
    print(f)
   