

class node:
    def __init__(self,name):
        self.name=name
        self.voisins=[]
        self.color=0
    
    def setliens(self,liste):
        for i in liste:
            self.voisins.append(i)
        self.voisins.sort(key=lambda node:node.color)
    
    def setcolor(self,col):
        self.color=col
        
    def aretes(self):
        T=[]
        for voisin in self.voisins:
            T.append((self.name,voisin.name))
        return T
    
    def getdsat(self):
        i=0
        n=0
        for v in self.voisins:
            if(v.color>n):
                i=i+1
                n=v.color
        return i


class graph:
    def __init__(self,list):
        self.noeuds=[]
        for i in list:
            self.noeuds.append(node(i))
    
    def affiche(self):
        for i in self.noeuds:
            print(i.name)
            
    def setvoisins(self,n,list):
        self.noeuds[n-1].setliens(list)

    def afficherarete(self):
        for nd in self.noeuds:
            print(nd.aretes())
            print("voici sa couleur:"+str(nd.color))
            print("voici sa dsat:"+str(nd.getdsat()))
    
    def ordredecroissant(self):
        self.noeuds.sort(key=lambda node:node.name,reverse=True)
        
    def checkmaxdsat(self):
        nb=node(0)
        for noeud in self.noeuds:
            if((noeud.getdsat()>nb.getdsat() or (noeud.name>nb.name and noeud.getdsat()==nb.getdsat())) and noeud.color==0):
                nb=noeud
        return nb
    
    def graphelem(self,n):
        return self.noeuds[n-1]
    
    def iscolorzero(self):
        for i in self.noeuds:
            if(i.color==0):
                return True
        return False

    
g=graph([1,2,3,4,5,6,7,8])
n=4
g.setvoisins(1,[g.graphelem(2),g.graphelem(3),g.graphelem(4),g.graphelem(5)])
g.setvoisins(2,[g.graphelem(3),g.graphelem(4),g.graphelem(1),g.graphelem(6)])
g.setvoisins(3,[g.graphelem(1),g.graphelem(2)])
g.setvoisins(4,[g.graphelem(1),g.graphelem(2)])
g.setvoisins(5,[g.graphelem(1),g.graphelem(7),g.graphelem(8)])
g.setvoisins(6,[g.graphelem(2),g.graphelem(8),g.graphelem(7)])
g.setvoisins(7,[g.graphelem(6),g.graphelem(8),g.graphelem(5)])
g.setvoisins(8,[g.graphelem(5),g.graphelem(7),g.graphelem(6)])
g.ordredecroissant()
j=1
g.noeuds[0].setcolor(j)
j=j+1
while(g.iscolorzero()):
    print("_____________________________________________________")
    g.checkmaxdsat().setcolor(j)
    print("we set la couleur"+str(j))
    print("le noeud à colorier est "+str(g.checkmaxdsat().name))
    if(j>=n):
        j=1
    else:
        j=j+1
    g.afficherarete()
    
    
    
    
    