import getDataIndicateur as gDI
import json
import codecs
jsonopen=open("traceforum.json", "r")
f = json.load(jsonopen)

listeUser= gDI.listeUstilisateur(f["transition"])
dicoUser=gDI.creationDicoUser(listeUser)
dicoUser=gDI.calculNbConnexionNbMsgPoste(dicoUser,f["transition"])
dicoEleve,dicoEnseignant, dicoInactif = gDI.separationEleveEnseignant(dicoUser,listeUser,f["transition"])
print("############prof############")
for cle,valeur in dicoEnseignant.items():
     print(cle)

print("##########eleve###########")
for cle,valeur in dicoEleve.items():
     print(cle)

print("###########inactif##########")
for cle,valeur in dicoInactif.items():
     print(cle)

print(dicoEleve)
jsonopen.close()