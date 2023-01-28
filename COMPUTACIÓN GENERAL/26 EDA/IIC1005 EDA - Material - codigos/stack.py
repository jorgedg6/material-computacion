class Stack():
    def __init__(self):
        #Pista: usar una lista como atributo
        self.elems = []
    def push(self,e):
        #Ponerlo el ultimo
        self.elems.insert(len(self.elems),e)
    def pop(self):
        #Sacar el ultimo
        return self.elems.pop(len(self.elems)-1)
    def size(self):
        return len(self.elems)


x = Stack()

x.push("abeja")
x.push("burro")
x.push("conejo")
print(x.size())

e = x.pop()
print(e)
print(x.size())

e = x.pop()
print(e)
print(x.size())


