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
        ''' Renvoie True si l'arbre binaire est vide, False s'il ne l'est pas. '''
        pass
    
    def racine(self):
        ''' Renvoie le Noeud racine de l'arbre binaire.
        :CU: L'arbre n'est PAS vide '''
        pass
    
    def valeur_racine(self):
        ''' Renvoie la valeur de la racine de l'arbre binaire.
        :CU: L'arbre n'est PAS vide'''
        pass
    
    def gauche(self):
        ''' Renvoie le sous-arbre gauche de l'arbre binaire.
        :CU: L'arbre n'est PAS vide'''
        pass
    
    def droite(self):
        ''' Renvoie le sous-arbre droit de l'arbre binaire.
        :CU: L'arbre n'est PAS vide'''
        pass
    
    def est_feuille(self):
        ''' Renvoie True si l'arbre binaire est une feuille, False s'il ne l'est pas.
        :CU: L'arbre n'est PAS vide'''
        pass