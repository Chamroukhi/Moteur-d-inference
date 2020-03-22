

#Base des régles
Regle=[]

#Base des Faits
Base_Fait =[]

#liste des regle applicable 
Regle_applicable=[]

#liste des nouveaux faits a ajouter(aprés_exécution)
NV=[]

#extraction des régles a partir d'un fichier BR.txt
with open("BR.txt","r+") as fichier:
    for line in fichier:
        #éliminer la retour en ligne
        res=line.replace('\n','')
        #éliminer les espaces
        res=res.replace(' ','')
        #séparer les premisses et les conclusion
        res=res.split("->")
        #ajouter tous les regle a la liste Regle[]
        Regle.append(res)
        
 
  
#extraction des faits a partir d'une fichier BF.txt
with open("BF.txt","r+") as faits:
    for line in faits:
        res=line.replace('\n','')
        res=res.split(",")
        Base_Fait.append(res)
        
#l'ensemble des faits       
Faitt=Base_Fait[0]

      
def masque_redondance(liste):
    """fonction pour eliminer la redondance"""
    new_list = [] 
    for i in liste : 
        if i not in new_list: 
            new_list.append(i)      
    return new_list


def ajout_nouveau_fait(old_liste,liste_a_ajouter):
    """fonction pour ajouter les conclusion d'une regle exécuté a la base des Faits
       avec élimination de redondance"""
    for i in liste_a_ajouter : 
        if i not in old_liste: 
            old_liste.append(i)
    return old_liste



    
#chainage_avant:
def chainage_avant(Base_regle,Base_faits):

  but ='H'
  print("BUT: ",but)
  C=0
  #while but not atteint 
  while (Base_faits[-1]!=but): 
    
    for i in range(len(Base_regle)):
       if (Base_faits[-1]!=but):
           #conclusion
           conclusion=Regle[i][1]
           conclusion=conclusion.split(",")
           #premises
           premise=Regle[i][0]
           premise=premise.split(",")
           
           #verifier si tous les valeur de premises sont 
           #trouver dans la base des faits ou non
           if (set(premise) -set(Base_faits)) == set() :
               
               for c in range(len(conclusion)):
                   #selectionner tous les valeur de conclusion 
                   #de la régle exécuté
                   NV.append(conclusion[c])
                   
               #cycle d'inférence    
               C=C+1
               print("Cycle d'inférence numéro:",C)
               
               #ajouter les regles applicable 
               Regle_applicable.append(i)
               
               print("================ Ensemble des faits initiale =====================")
               print(Faitt) 
               
               #ajouter les faits trouver a la base des faits
               Base_faits=ajout_nouveau_fait(Base_faits,NV) 
               
               print("================ Ensemble de régles applicable ===================")
               print(masque_redondance(Regle_applicable),"=>",Regle[i])
               
               print("================ Bases des faits aprés MAJ =======================")
               print(Faitt)
               print("\n")
               print("\n")
               
        
                     
       
#les régles 
print("====================== Ensemble des régles :=======================\n")
for i in range (len(Regle)):
    print("R",i,": ",Regle[i])
    
    
chainage_avant(Regle, Faitt)



print("But atteint :)")


    




     




            