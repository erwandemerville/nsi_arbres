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
    
    pass

def hauteur(a: Arbre) -> int:
    ''' Renvoie la hauteur d'un arbre. '''
    
    pass

def nb_feuilles(a: Arbre) -> int:
    ''' Renvoie le nombre de feuilles que contient un arbre binaire. '''
    
    pass

def est_present(a: Arbre, el: 'int|str') -> bool:
    ''' Renvoie True si un noeud contenant l'élément el est présent dans l'arbre, False sinon. '''
    
    pass

# Fonctions de parcours d'arbres

def parcours_prefixe(a: Arbre) -> None:
    ''' Affiche les valeurs des noeuds de l'arbre parcourus en ordre préfixe. '''
    
    pass

def parcours_suffixe(a: Arbre) -> None:
    ''' Affiche les valeurs des noeuds de l'arbre parcourus en ordre suffixe. '''
    
    pass

def parcours_infixe(a: Arbre) -> None:
    ''' Affiche les valeurs des noeuds de l'arbre parcourus en ordre infixe. '''
    
    pass

def parcours_en_largeur(a: Arbre) -> None:
    ''' Affiche les valeurs des noeuds de l'arbre parcourus en largeur.
    :CU: L'arbre a est NON VIDE '''
    
    pass


if __name__ == '__main__':
    ''' Instructions exécutées si l'on exécute ce fichier directement '''
    
    pass