class Queue():
    def __init__(self):
        #Pista: usar una lista como atributo
        self.elems = []
    def enqueue(self,e):
        #Ponerlo el ultimo
        self.elems.insert(len(self.elems),e)
    def dequeue(self):
        #Sacar el primero
        return self.elems.pop(0)
    def size(self):
        return len(self.elems)


x = Queue()

x.enqueue("abeja")
x.enqueue("burro")
x.enqueue("conejo")
print(x.size())

e = x.dequeue()
print(e)
print(x.size())

e = x.dequeue()
print(e)
print(x.size())


