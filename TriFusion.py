Liste = [3,6,2,8,10,5,14]

def TriFusion(Liste):
    TailleTotale = len(Liste)
    
    if TailleTotale == 0 or TailleTotale == 1:
        return []
    else :
        milieu = TailleTotale // 2
        PartieG = Liste[0:milieu]
        PartieD = Liste[milieu:TailleTotale]
        
        TriFusion(PartieG)
        TriFusion(PartieD)
        
        indiceListe = 0
        indiceG = 0
        indiceD = 0
        
        while indiceG < len(PartieG) and indiceD < len(PartieD):
            if PartieG[indiceG] < PartieD[indiceD]:
                Liste[indiceListe] = PartieG[indiceG]
                indiceG += 1
            else :
                Liste[indiceListe] = PartieD[indiceD]
                indiceD += 1
            indiceListe += 1
        
        while indiceD < len(PartieD):
            Liste[indiceListe] = PartieD[indiceD]
            indiceD += 1
            indiceListe += 1
            
        while indiceG < len(PartieG):
            Liste[indiceListe] = PartieG[indiceG]
            indiceG += 1
            indiceListe += 1
            
            
TriFusion(Liste)
print(Liste)
                
        
        
        
    
                
        