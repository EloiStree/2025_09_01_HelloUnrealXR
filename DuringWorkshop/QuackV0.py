 
import time
import os
print("Quack")
canard_champagne ="è§&\"à\"§çé§'§&"
pile = "('àà&'&'àç'(&"
score = 0 
objet_deja_utilise = []
while True : 
    print ("scanne un nouvelle objet") 
    #"time.sleep(1)
    objet_scan = input()
    print (objet_scan)
    wrong_object=False
    for id in objet_deja_utilise :

        if id == objet_scan : 
            print ("salaud")
            #os._exit(1)
            wrong_object=True

        

    if wrong_object:
        print ("deja utilise")
    elif objet_scan==canard_champagne:     
        print("winner Champagne bottle")
    elif objet_scan== pile:
        print ("biere")
    else: 
        print ( "5 point")
        score = score + 5
        print ("bravo tu es as score"+ str(score)) 
    objet_deja_utilise.append(objet_scan)
