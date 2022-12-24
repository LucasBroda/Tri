Liste = [10,5,1,3,7,22,67,30]




def TriRapide(Liste):
    def trirap(Liste, g, d):
        pivot = Liste[(g+d)//2]
        i = g
        j = d
        while True:
            while Liste[i]<pivot:
                i+=1
            while Liste[j]>pivot:
                j-=1
            if i>j:
                break
            if i<j:
                Liste[i], Liste[j] = Liste[j], Liste[i]
            i+=1
            j-=1
        if g<j:
            trirap(Liste,g,j)
        if i<d:
            trirap(Liste,i,d)
 
    g=0
    d=len(Liste)-1
    trirap(Liste,g,d)
    

TriRapide(Liste)
print(Liste)