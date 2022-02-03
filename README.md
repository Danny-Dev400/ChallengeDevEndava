# ChallengeDevEndava
Aplicar programacion dinamica a un problema generado por la empresa

# Explicacion del algoritmo 

## Complejidad Temporal: 

El algoritmo se divide en 5 faces: 

- La primera es la apertura del archivo el cual es un ciclo que recorre linea a linea el archivo y lo va añadiendo a dos listas, Una de Nodos(Identificador del lugar a limpiar) y otra para los Valores(cantidad de basura en el cuarto) por lo tanto su complejidad es O(n) 

- La segunda contempla la creacion  de la lista de adyacencia la cual es una iteracion anidada, son 2 iteraciones por lo cual la complejidad es O((n/2)^2) 

- La tercera fase es un ordenamiento topologico el cual su complejidad temporal esta dada por la cantidad de vertices(n) sumado a la cantidad de aristas(m), asi que la complejidad de este ordenamiento seria:  O(n+m) 

- La Cuarta fase es la recorrer una vez los vertices del grafo para tomar los vertices con mayor longitud en su Camino.  O(n) 

- Por ultimo Imprimir la ruta encontrada de cada uno de estos nodos ( para esta implementacion solo imprime la primera ruta mas larga)  con mayor longitud de camino en un archivo ‘result.txt’ con complejidad O(n) 

## Complejidad total del algoritmo es:  O((n/2)^2) + 3O(n) + O(n+m) 

 

## Complejidad espacial: 

La complejidad de la lista de adyacencia tiene su complejidad espacial en la cantidad de vertices(n) multiplicado por la cantidad de aristas(m). Es decir tiene complejidad: O(n*m)  
