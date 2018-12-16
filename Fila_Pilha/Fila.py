class queue:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.__tamanho = 0
        self.__iterando = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__iterando is None:
            self.__iterando = self.primeiro
        else:
            self.__iterando = self.__iterando.proximo

        if self.__iterando is not None:
            return self.__iterando.dado

        raise StopIteration

    def __len__(self):
        return self.__tamanho

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        retorno = '['
        for i, e in enumerate(self):
            retorno += e.__repr__()
            if i < len(self) - 1:
                retorno += ', '

        retorno += ']'
        return retorno

    class No:
        def __init__(self,dado):
            self.dado = dado
            self.proximo = None

    def __insert(self,valor):
        novo = self.No(valor)
        if self.primeiro == None:
            self.primeiro = self.ultimo = novo
        else:
            self.ultimo.proximo = novo
            self.ultimo = novo

        self.__tamanho += 1
        self.__iterando = None



    def enqueue(self,valor):
        self.__insert(valor)

    def __delitem__(self,i):
        atual = self.primeiro
        if i == 0:
            self.primeiro = atual.proximo
            atual.proximo = None
        else:
            print('Não permitido!')

        self.__iterando = None
        self.__tamanho -= 1

    def denqueue(self):
        del self[0]

queue = queue()
queue.enqueue('Jonas')
queue.enqueue('Manoel')
queue.enqueue('Inácio')
queue.enqueue('Eduardo')

print(queue)

queue.denqueue()
print(queue)
queue.denqueue()
print(queue)
queue.denqueue()
print(queue)
queue.denqueue()
print(queue)