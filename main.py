from scipy import *
#Permet de renvoyer le nombre de connexion ainsi que le nombre de message posté
def calculNbConnexionNbMsgPoste(nomuser,data):
    compteurConnexion=0
    compteurMsgPoste=0
    for item in data :
        if item.nomuser == nomuser and item.action == "Connexion":
            compteurConnexion+=1
        elif item.nomuser == nomuser and item.action == "Poster un nouveau message":
            compteurMsgPoste+=1
    return compteurConnexion,compteurMsgPoste

#Permet de renvoyer le nombre de connexion ainsi que le nombre de message posté de référence
def calculNbConnexionNbMsgPosteReference(listeUser,data):
    tauxCompteurConnexion=0
    compteurMsgPoste = 0
    for item in data :
        if item.action == "Connexion":
            tauxCompteurConnexion+=1
        elif item.action == "Poster un nouveau message":
            compteurMsgPoste+=1
    return (tauxCompteurConnexion / listeUser.len()),(compteurMsgPoste / listeUser.len())

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


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('aurélien')

