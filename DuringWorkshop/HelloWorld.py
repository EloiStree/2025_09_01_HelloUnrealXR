print ("hello world")
mes_eleves=[]
for compteur in range (6):
    nom_utilisateur = input("Entrez votre nom : ")
    age= input("Quel est ton age?")
    try:
        if float(age) < 0:
            print("salaud!")
            exit()
    except: 
        print("g pa compri")
    mes_eleves .append (nom_utilisateur+" " + age)        
    for un_eleve in mes_eleves:
        print (un_eleve)
