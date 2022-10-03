

class PilhaException(Exception):
    def __init__(self, mensagem: object) -> None:
        super().__init__(mensagem)
class No:
    def __init__(self,carga:any):
        self.carga = carga
        self.prox = None
    def __str__(self):
        return str(self.carga)



class Pilha:
    def __init__(self):
        self.__start = None
        self.__tamanho = 0
    #verifica se a pilha está vazia
    def estaVazia(self):
        return self.__start==None
    #retorna o tamanho da pilha, O while percorrer toda Pilha, se só vai parar quando o cursor ser == None, já que ele cursor recebe cursosr.prox
    #ele vai até o final da pilha.
    def tamanho(self):
        cont = 0
        cursor = self._start
        while(cursor != None):
            cont += 1
            cursor = cursor.prox
        return cont
    #função que retorna a carga da posicção escolhida pelo usuário.
    def elemento(self,posicao):
        try:
            assert posicao > 0 and posicao < self.__tamanho
            #aritimetica para saber quantos passos dar até tal posição.
            deslocamento = self.__tamanho - posicao
            cont = 0
            #o cursor começão no começo da pilha
            cursor = self.__start
            #Enquanto o deslocamento  ser maior que o cont, o cursor avança uma posição.
            while(deslocamento > cont):
                cont += 1
                cursor = cursor.prox
            return cursor.carga
        except:
            raise PilhaException(f'Posição Inválida!!! a Pilha atual com {self.__tamanho} elementos')

        
    # percorrer toda pilha procurando o conteúdo igual o escolhido pelo usuário, 
    # caso encontre retorna a posição do elemento, com referencia da base sendo o fim da pilha.
    def busca(self,conteudo):
        cont = 0
        cursor = self.__start
        while(cursor != None):
            if cursor.carga == conteudo:
                return self.__tamanho - cont
            cont += 1
            cursor = cursor.prox
        return cont
        raise PilhaException('Conteúdo Não encontrado!')
    #Função que modificar uma carga, na posição escolhida pelo usuário e sobrescrever a carga de tal posição com o conteúdo fornecido pelo mesmo.
    def modificar(self,posicao,conteudo):
        try:
            assert posicao > 0 and posicao <= self.__tamanho
            deslocamento = self.__tamanho - posicao
            cont = 0
            cursor = self.__start
            while(deslocamento > cont):
                cont += 1
                cursor = cursor.prox
            cursor.carga = conteudo
            

        except:
            pass
    #empihlar elementos na pilha, faz o próximo do novo elemento apontar para o topo, e faz o topo ser agora o novo e incrementa o tamanho.
    def empilhar(self,valor):
        novo = No(valor)
        novo.prox = self.__start
        self.__start = novo 
        self.__tamanho += 1
        
    #remove elementos do topo da pilha, caso ela está com elemento
    def desempilhar(self):
        if self.estaVazia():
            raise PilhaException('Pilha Vazia, impossível desempilhar!')
        pop = self.__start.carga
        self.__start = self.__start.prox
        self.__tamanho -= 1
        return pop
    #imprime a pilha
    def __str__(self):
       s = '['
       cursor = self.__start
       while(cursor != None):
            s += f' {cursor.carga}'
            cursor = cursor.prox
       s += '] <-topo'
       return s
    #Esvazia a pilha um de cada vez, até fica vazia(start == None)
    def esvazia(self):
        while(not self.estaVazia()):
            self.desempilhar()    