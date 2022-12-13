from dessin import dessiner

''' Classe implémentant un Arbre Binaire. '''

class Arbre:
    def __init__(self, valeur=None, gauche=None, droite=None):
        ''' Crée un nouvel arbre binaire.
        :param valeur: (int|str) La valeur du noeud racine, soit un entier, soit une chaîne de caractères
        :param gauche: (Arbre) Le sous-arbre binaire gauche (None pour arbre binaire vide)
        :param droite: (Arbre) Le sous-arbre binaire droit (None pour arbre binaire vide)
        :CU: Si valeur est à None, gauche et droite doivent être également à None (cas de l'arbre vide),
        sinon, gauche et droite doivent être de type Arbre. '''
        
        assert (valeur == None and gauche == None and droite == None) or \
               (type(valeur) in (int, str) and type(gauche) == Arbre and type(droite) == Arbre)
        
        self.v = valeur
        self.g = gauche
        self.d = droite

    def est_vide(self):
        ''' Renvoie True si l'arbre binaire est vide, False s'il ne l'est pas.
        :param self: (Arbre) L'arbre binaire
        :return: (bool) True ou False selon si l'arbre est vide ou non '''
        
        return self.v == None
        # Si la valeur du noeud racine est à None, le sous-arbre gauche et droit le sont également (donc l'arbre est vide)
    
    def racine(self):
        ''' Renvoie le Noeud racine de l'arbre binaire.
        :param self: (Arbre) L'arbre binaire dont on veut récupérer la racine
        :return: (Arbre) Le noeud racine de l'arbre
        :CU: L'arbre n'est PAS vide '''
        
        return self
    
    def valeur_racine(self):
        ''' Renvoie la valeur de la racine de l'arbre binaire.
        :param self: (Arbre) L'arbre binaire dont on veut récupérer la valeur racine
        :return: (int|str) La valeur contenue dans le noeud racine de l'arbre
        :CU: L'arbre n'est PAS vide '''
        
        return self.v
    
    def gauche(self):
        ''' Renvoie le sous-arbre gauche de l'arbre binaire.
        :param self: (Arbre) L'arbre binaire dont on veut récupérer le ss-arbre gauche
        :return: (Arbre) Le sous-arbre gauche
        :CU: L'arbre n'est PAS vide '''
        
        return self.g
    
    def droite(self):
        ''' Renvoie le sous-arbre droit de l'arbre binaire.
        :param self: (Arbre) L'arbre binaire dont on veut récupérer le ss-arbre droit
        :return: (Arbre) Le sous-arbre droit
        :CU: L'arbre n'est PAS vide '''
        
        return self.d
    
    def est_feuille(self):
        ''' Renvoie True si l'arbre binaire est une feuille, False s'il ne l'est pas.
        :param self: (Arbre) L'arbre binaire
        :return: (bool) True ou False selon si l'arbre est une feuille ou non
        :CU: L'arbre n'est PAS vide '''
        
        return self.gauche().est_vide() and self.droite().est_vide()
    
# Quelques mesures et prédicats sur les arbres

def taille(a: Arbre) -> int:
    ''' Renvoie la taille d'un arbre. '''
    
    if a.est_vide():
        return 0
    else:
        return 1 + taille(a.gauche()) + taille(a.droite())

def hauteur(a: Arbre) -> int:
    ''' Renvoie la hauteur d'un arbre. '''
    
    if a.est_vide():
        return -1
    else:
        return 1 + max(hauteur(a.gauche()), hauteur(a.droite()))

def nb_feuilles(a: Arbre) -> int:
    ''' Renvoie le nombre de feuilles que contient un arbre NON VIDE. '''
    
    if a.est_vide():
        return 0
    elif a.est_feuille():
        return 1
    else:
        return nb_feuilles(a.gauche()) + nb_feuilles(a.droite())

def est_present(a: Arbre, el: int|str) -> bool:
    ''' Renvoie True si un noeud contenant l'élément el est présent dans l'arbre, False sinon. '''
    
    if a.est_vide():
        return False
    elif a.valeur_racine() == el:
        return True
    else:
        return est_present(a.gauche()) or est_present(a.droite())

# Fonctions de parcours d'arbres

def parcours_prefixe(a: Arbre) -> None:
    ''' Affiche les valeurs des noeuds de l'arbre parcourus en ordre préfixe. '''
    
    print(a.valeur_racine())
    if not a.gauche().est_vide():
        parcours_prefixe(a.gauche())
    if not a.droite().est_vide():
        parcours_prefixe(a.droite())
        
def parcours_prefixe_l(a: Arbre) -> list:
    ''' Renvoie une liste des valeurs des noeuds de l'arbre parcourus en ordre préfixe. '''
    
    res = [a.valeur_racine()]
    if not a.gauche().est_vide():
        res += parcours_prefixe_l(a.gauche())
    if not a.droite().est_vide():
        res += parcours_prefixe_l(a.droite())
    return res

def parcours_suffixe(a: Arbre) -> None:
    ''' Affiche les valeurs des noeuds de l'arbre parcourus en ordre suffixe. '''
    
    if not a.gauche().est_vide():
        parcours_suffixe(a.gauche())
    if not a.droite().est_vide():
        parcours_suffixe(a.droite())
    print(a.valeur_racine())
    
def parcours_suffixe_l(a: Arbre) -> list:
    ''' Renvoie une liste des valeurs des noeuds de l'arbre parcourus en ordre suffixe. '''
    
    res = []
    if not a.gauche().est_vide():
        res += parcours_suffixe_l(a.gauche())
    if not a.droite().est_vide():
        res += parcours_suffixe_l(a.droite())
    res += [a.valeur_racine()]
    return res

def parcours_infixe(a: Arbre) -> None:
    ''' Affiche les valeurs des noeuds de l'arbre parcourus en ordre infixe. '''
    
    if not a.gauche().est_vide():
        parcours_infixe(a.gauche())
    print(a.valeur_racine())
    if not a.droite().est_vide():
        parcours_infixe(a.droite())
        
def parcours_infixe_l(a: Arbre) -> list:
    ''' Renvoie une liste des valeurs des noeuds de l'arbre parcourus en ordre infixe. '''
    
    res = []
    if not a.gauche().est_vide():
        res = parcours_infixe_l(a.gauche())
    res += [a.valeur_racine()]
    if not a.droite().est_vide():
        res += parcours_infixe_l(a.droite())
    return res

def parcours_en_largeur(a: Arbre) -> None:
    ''' Affiche les valeurs des noeuds de l'arbre parcourus en largeur.
    :CU: L'arbre a est NON VIDE '''
    
    file = []
    file.append(a.racine())
    while len(file) != 0:
        n = file.pop(0)
        print(n.valeur_racine())
        if not n.gauche().est_vide():
            file.append(n.gauche())
        if not n.droite().est_vide():
            file.append(n.droite())
    
if __name__ == '__main__':
    ''' Instructions exécutées si l'on exécute ce fichier directement '''
    
    a = Arbre('C', Arbre('A', Arbre(), Arbre('H', Arbre('D', Arbre(), Arbre()), Arbre('F', Arbre(), Arbre()))), Arbre('B', Arbre('G', Arbre(), Arbre()), Arbre('E', Arbre(), Arbre())))