#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Ajouter les imports nécessaires. 

"""

def index_documents(docs_df,stopwords):
    """ 
    A partir du dataFrame des documents, va constituer l'index inversé 
    (terme x documents) qui donne pour chaque terme, la liste des documents
    dans lesquels il apparait. On prend les termes présent dans le titre,
    les auteurs, et la conférence. On enlève les stopwords (fichier common_words)
    
    AIDE: ATTENTION, pensez à la suppression des stopwords.
    On parcourt l'ensemble des documents du dataframe, on découpe
    chaque chaines de caractères en mots, des colonnes titres, auteur, et conférence.
    On insert ce terme dans une hashmap (dictionnaire python) en clé et la valeur
    est la liste des documents où le terme est apparu.
    Le dictionnaire est sous la forme {"termeX": [1,2,3,7],"termeY":[1,4] etc...}

    Parameters
    ----------
    docs_df : pandas.Dataframe
        le dataframe construit avec utils.load_documents
    
    stopwords: list/dictionanry
        liste des stopwords à éliminer

    Returns
    -------
    docx_index : dictionnary
        le dictionnaire représentant l'index inversé avec en clé chaque terme
        et en valeur chaque document où il apparait.

    """   
    docs_index = None
    return docs_index