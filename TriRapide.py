Liste = [10,5,1,3,7,22,67,30]


def tri(Liste,debut,fin):
    pivot = Liste[fin]
    indice = debut
    
    for i in range(debut,fin):
        if Liste[i] <= pivot:
            Liste[i],Liste[indice] = Liste[indice], Liste[i]
            indice += 1
            
    Liste[indice], Liste[fin] = Liste[fin], Liste[indice]
    return indice


def TriRapide(Liste,debut = 0, fin = None):
    if fin == None:
        fin = len(Liste)-1
    
    if fin>debut:
        pivot = tri(Liste,debut,fin)
        #Cherche le pivot
        
        TriRapide(Liste,debut,pivot-1)
        #Tri de la partie gauche
        
        TriRapide(Liste,pivot+1,fin)
        #Tri de la partie droite
        

       
TriRapide(Liste)
print(Liste)
        