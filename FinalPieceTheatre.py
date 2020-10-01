def miseEnPlace(rang,apres,acteur):
    """
    Fonction dont le but est de placer chacun des acteurs qui entrent successivement sur scène à l'endroit qui convient, pour former un rang sur la scène en vue de la présentation finale.

    Paramètres :

    rang = le rang en cours de formation
    apres = position que va prendre un acteur dans le rang (chaîne de caractères)
        valeurs possibles :
        soit "" lorsque le premier acteur vient se placer ou lorsqu'un acteur vient se placer à gauche du rang
        soit Ax, x étant le numéro de l'acteur après lequel il doit venir se placer (ex : "A6")
    acteur = nom de la variable correspondant à un acteur (tuple). Exemple : acteur5.

    Renvoie le rang avec un nouvel acteur positionné.
    """

    if apres=="" and acteur==():
        return rang

    elif apres=="" and acteur!=(): # placement en début de rang
        return (acteur[0],rang)

    else:
        tmp=()

        while rang[1]!=() and rang[0]!=apres:
            tmp=(rang[0],tmp)
            rang=rang[1]

        if rang[1]==(): # placement en fin de rang
            x=(rang[0],(acteur[0],()))
            while tmp[1]!=():
                x=(tmp[0],x)
                tmp=tmp[1]
            return (tmp[0],x)

        else: # placement entre deux acteurs
            if tmp==(): # ou if rang[0]==apres | placement après le premier
                return (rang[0],(acteur[0],(rang[1])))
            else:
                x=(rang[0],(acteur[0],(rang[1])))
                while tmp[1]!=():
                    x=(tmp[0],x)
                    tmp=tmp[1]
                return (tmp[0],x)

def afficheRang(rang):
    """
    Affiche le rang des acteurs selon leur ordre d'arrivée sur scène et leur positionnement dans le rang.
    """
    if rang!=():
        x="<< "+rang[0]+" >>"
        while rang[1]!=():
            rang=rang[1]
            x=x+"<< "+rang[0]+" >>"
        print(x)
    else:
        print("Aucun acteur sur scène")