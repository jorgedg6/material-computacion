class Playlist:
    def __init__(self):
        self.cs = []
        self.gs = []

    def agregar(self,c,g):
        self.cs.append(c)
        self.gs.append(g)

    def __str__(self):
        txt = "--PLAYLIST--\n"
        for i in range(0,len(self.cs)):
            txt = txt + self.cs[i] + " - " + self.gs[i] + "\n"
        txt = txt + "------------"
        return txt
        


#CODIGO PRINCIPAL
p = Playlist()

p.agregar("All The Small Things","Blink 182")
p.agregar("Song2","Blur")
p.agregar("Still Waiting","Sum 41")
p.agregar("When I Come Around","Green Day")

print(p)

print(p)
        

