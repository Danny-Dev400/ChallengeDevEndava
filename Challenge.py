
from datetime import datetime
import random

#class vertice
class Vertice:
    #constructor
    def __init__(self, i, Valor):
        self.id = i
        self.valor = Valor
        self.visit = False
        self.grado = 0
        self.lp = 0
        self.path = []
        self.vecinos = []

    def addVecino(self, v):
        if not v in self.vecinos:
            self.vecinos.append(v)

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.grafoOrdenado = []
        self.longitudLp = 0

    def addVertice(self, v, nivel):
        if not v in self.vertices:
            self.vertices[v] = Vertice(v, nivel)

    def addArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].addVecino(b)
            #self.vertices[b].addVecino(a)

    def khanSort(self):
        copyGrafo = self.vertices.copy()
        s=[]
        for nodo in copyGrafo:
            if copyGrafo[nodo].grado == 0:
                s.append(nodo)

        while len(s) != 0:
            nodoSalida = s.pop(0)
            self.grafoOrdenado.append(nodoSalida)

            for nodoAdj in copyGrafo[nodoSalida].vecinos:
                copyGrafo[nodoAdj].grado -= 1
                if copyGrafo[nodoSalida].lp >= copyGrafo[nodoAdj].lp:
                    copyGrafo[nodoAdj].lp += 1
                    self.longitudLp = copyGrafo[nodoAdj].lp
                    copyGrafo[nodoAdj].path = copyGrafo[nodoSalida].path.copy()
                    copyGrafo[nodoAdj].path.append([nodoSalida,nodoAdj])

                if copyGrafo[nodoAdj].grado == 0:
                    s.append(nodoAdj)

def main():
    
    archivo = "input.txt"

    archivo = input()

    start_time = datetime.now()
    Nodos = []
    Valores = []
    n = 0

    with open(archivo) as archivo:
        lines = list(archivo.readlines())
        n = lines[0]
        for line in lines[1:]:
            lugar, cantidadBasura = line.split(',')
            try:
                Nodos.append(lugar)
                Valores.append(int(cantidadBasura))
            except:
                print('El archivo suministrado no cumple con los requerimientos, Contiene Cantidad de basura no numerica')
                return None
    if len(Nodos) == 0:
        print("El archivo suministrado no cumple con los requerimientos, se encuentra vacio")
        return None

    """
    Nodos = []
    Valores = []

    n=10

    for i in range(n+1):
        Nodos.append(i)
        Valores.append(random.randint(1,10000))
    """

    g = Grafo()

    """
    Nodos = ["Elevator","Hall","Pingpong","Cafeteria","Terrace","Terrace Ofices", "cosa"]
    Valores = [57,889,546,867,587,34,35]
    """
    for v in range(0,len(Nodos), 1):
        g.addVertice(Nodos[v],Valores[v])

    cont = 0
    
    for a in range(0,len(Valores), 1):
        for b in range(cont,len(Valores), 1):
            if Valores[a] > Valores[b]:
                g.addArista(Nodos[a],Nodos[b])
                g.vertices[Nodos[b]].grado += 1
        cont+=1

    g.khanSort()

    listaDeFinales = []
    for nodo in g.vertices:
        if g.vertices[nodo].lp == g.longitudLp:
            listaDeFinales.append(nodo)
            break

    #for v in g.vertices:
    #   print(v, g.vertices[v].valor , g.vertices[v].vecinos, g.vertices[v].grado, g.vertices[v].lp, g.vertices[v].path)

    final = []
    for item in g.vertices[listaDeFinales[0]].path:
        final.append(str(item[0]))
    final.append(str(g.vertices[listaDeFinales[0]].path[-1][1]))

    with open('result.txt','w') as file:
        file.write(str(len(final))+'\n')
        for lugar in final:
            file.write( str(g.vertices[lugar].id) + ', ' + str(g.vertices[lugar].valor) + '\n')

    print(final)
    print(f"BFS ended in : {datetime.now() - start_time} seconds")

   #cosa = Valores.pop(0)
   #print(cosa)

main()




