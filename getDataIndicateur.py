from scipy import *
#Permet de renvoyer le nombre de connexion ainsi que le nombre de message posté
def calculNbConnexionNbMsgPoste(listeuser,data):
    for item in data :
        if  item["Titre"] == "'Connexion'":
            listeuser[item["Utilisateur"]]['compteurConnexion']+=1
        elif item["Titre"] == "'Poster un nouveau message'":
            listeuser[item["Utilisateur"]]['compteurMsgPoste']+=1
    return listeuser

def listeUstilisateur(data):
    listeUser=[]
    for item in data : 
        listeUser.append(item["Utilisateur"])
        listeUser[:]=list(set(listeUser))
    return listeUser

def creationDicoUser(listeuser):
    dicoUser={}
    for item in listeuser :
        dicoUser[item]={'compteurConnexion' : 0,'compteurMsgPoste' : 0}
    return dicoUser

#Permet de renvoyer le nombre de connexion ainsi que le nombre de message posté de référence
def calculNbConnexionNbMsgPosteReference(listeUser,data):
    tauxCompteurConnexion=0
    compteurMsgPoste = 0
    for item in data :
        if item["Titre"]== "'Connexion'":
            tauxCompteurConnexion+=1
        elif item["Titre"] == "'Poster un nouveau message'":
            compteurMsgPoste+=1
    return (tauxCompteurConnexion / len(listeUser)),(compteurMsgPoste / len(listeUser))

def moyenneHeureUtilisationSite(user,data):
    moyHeure=0
    tabidmsgenvoyer=[]
    date=0
    heure=0
    for item in data :
        if item.action == "Connexion" and user==item.nomuser:
            [tabidmsgenvoyer.append(item.date) for x in tabidmsgenvoyer if x not in tabidmsgenvoyer]
    debheure = zeros(len(tabidmsgenvoyer))
    tabdate=zeros(len(tabidmsgenvoyer))
    for date in tabidmsgenvoyer :
        for item in data :
            if user==item.nomuser and item.date==tabidmsgenvoyer[date]:
                if item.action == "Connexion" and debheure[date]==0:
                    debheure[date]=item.heure
                else:
                    tabdate[date] = item.heure
    tabheure = zeros(len(tabidmsgenvoyer))
    for date in tabdate:
        tabheure[date]=tabdate[date]-debheure[date]
    return tabdate
    

def calulDelaiReponseMessage(user,data):
    posternewmessagedate=[]
    posteridnewmessage=[]
    heure=0
    for item in data:
        if item.action=="Poster un nouveau message" and item.nomuser == user:
            [posternewmessagedate.append(item.date) for x in posternewmessagedate if x not in posternewmessagedate]
            posteridnewmessage.append(item.attribut.split(',')[1].split('=')[1])
    for item in posteridnewmessage :
        for ligne in data:
            if (ligne.attribut.split(',')[1].split('=')[1] == posteridnewmessage[item] and user==ligne.nomuseer) and (ligne.action=='Afficher le contenu d''un message' or ligne.action=='Afficher le contenu d''un message') :
                [posternewmessagedate.append(ligne.date) for x in posternewmessagedate if x not in posternewmessagedate]
                heure+=ligne.delai
    return heure / len(posternewmessagedate)


