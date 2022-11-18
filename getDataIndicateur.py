from scipy import *
#Permet de renvoyer le nombre de connexion ainsi que le nombre de message posté
def calculNbConnexionNbMsgPoste(dicoUser,data):
    for item in data :
        if  item["Titre"] == "'Connexion'":
            dicoUser[item["Utilisateur"]]['compteurConnexion']+=1
        elif item["Titre"] == "'Poster un nouveau message'":
            dicoUser[item["Utilisateur"]]['compteurMsgPoste']+=1
        elif item["Titre"] == "'Upload un ficher avec le message'":
            dicoUser[item["Utilisateur"]]['fichierUpload']+=1
        elif item["Titre"] == "'Répondre à un message'":
            dicoUser[item["Utilisateur"]]['compteurMsgRep']+=1
            
    return dicoUser

#Permet de récupérer la liste des utilisateurs 
def listeUstilisateur(data):
    listeUser=[]
    for item in data : 
        listeUser.append(item["Utilisateur"])
        listeUser[:]=list(set(listeUser))
    return listeUser

#Permet d'associer les utilisateurs aux différents indicateurs
def creationDicoUser(listeuser):
    dicoUser={}
    for item in listeuser :
        dicoUser[item]={'compteurConnexion' : 0,'compteurMsgPoste' : 0,'fichierUpload':0, 'compteurMsgRep':0}
    return dicoUser

#Permet de renvoyer le nombre de connexion ainsi que le nombre de message posté de référence
def moyenneFichierUploadAllPerson(listeUser,data):
    tauxCompteurConnexion=0
    compteurMsgPoste = 0
    compteurFichierUpload=0
    for item in data :
        if item["Titre"]== "'Connexion'":
            tauxCompteurConnexion+=1
        elif item["Titre"] == "'Poster un nouveau message'":
            compteurMsgPoste+=1
        elif item["Titre"] == "'Upload un ficher avec le message'":
            compteurFichierUpload+=1
    return (compteurFichierUpload / len(listeUser))

#Permet de récupérer un dictionnaire d'élève et un dictionnaire d'enseignant et un dictionnaire de personne inactif
def separationEleveEnseignant(dicoUser,listeUser,data):
    dicoEleve={}
    dicoEnseignant={}
    dicoCompteInactif={}
    valRefFichierUpload = moyenneFichierUploadAllPerson(listeUser,data)
    #On part du principe que les élèves ont posté beaucoup de message et intéragit plus sur le site par rapport au enseignant
    for item in listeUser:
        #On part sur inférieur a 10 car soit un prof soit inactif
        if(dicoUser[item]["compteurMsgPoste"]<10):
            #Si il y a des uploads c'est que c'est un élève
            if(dicoUser[item]["fichierUpload"]>valRefFichierUpload):
                dicoEleve[item]=dicoUser[item]
            #Si il n'y a pas de connexions ou de messages postés c'est que la personne est totalement inactif
            elif(dicoUser[item]["compteurConnexion"]==0 or dicoUser[item]["compteurMsgPoste"]==0 or item=="'admin'"):
                dicoCompteInactif[item]=dicoUser[item]
            #Si une personne après l'écrémage a moins de 5 messages on le compte comme un élève car les professeurs ont tendance à répondre aux élèves
            elif (dicoUser[item]["compteurMsgRep"]<=5):
                dicoEleve[item]=dicoUser[item]
            else :
                dicoEnseignant[item]=dicoUser[item]
        else :
            dicoEleve[item]=dicoUser[item]
    return dicoEleve,dicoEnseignant,dicoCompteInactif


#Permet de récupérer le nombre d'heure sur toutes les journées
def heureUtilisationSite(user,data):
    tabidmsgenvoyer=[]
    date=0
    for item in data :
        if item["Titre"] == "'Connexion'" and user==item["Utilisateur"]:
            [tabidmsgenvoyer.append(item["Date"]) for x in tabidmsgenvoyer if x not in tabidmsgenvoyer]
    debheure = zeros(len(tabidmsgenvoyer))
    tabdate=zeros(len(tabidmsgenvoyer))
    for date in tabidmsgenvoyer :
        for item in data :
            if user==item["Utilisateur"] and item["Date"]==tabidmsgenvoyer[date]:
                if item["Titre"] == "'Connexion'" and debheure[date]==0:
                    debheure[date]=item["Heure"]
                else:
                    tabdate[date] = item["Heure"]
    tabheure = zeros(len(tabidmsgenvoyer))
    for date in tabdate:
        tabheure[date]=tabdate[date]-debheure[date]
    return tabdate
    
#Permet de calculer le Delai entre l'envoie du premier message et l'affichage de la réponse au message
def calulDelaiReponseMessage(user,data):
    posternewmessagedate=[]
    posteridnewmessage=[]
    heure=0
    for item in data:
        if item["Titre"]=="'Poster un nouveau message'" and user==item["Utilisateur"]:
            [posternewmessagedate.append(item["Date"]) for x in posternewmessagedate if x not in posternewmessagedate]
            posteridnewmessage.append(item.attribut.split(',')[1].split('=')[1])
    for item in posteridnewmessage :
        for ligne in data:
            if (ligne.attribut.split(',')[1].split('=')[1] == posteridnewmessage[item] and user==item["Utilisateur"]) and (item["Titre"]=="'Afficher le contenu d\'\'un message'" or item["Titre"]=="'Répondre à un message'") :
                [posternewmessagedate.append(item["Date"]) for x in posternewmessagedate if x not in posternewmessagedate]
                heure+=ligne.delai
    return heure / len(posternewmessagedate)


