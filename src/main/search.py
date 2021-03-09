#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Ajouter les imports nécessaires. 
"""

def search_one_query(query,inversed_index,stopwords):
    """
    Prend en entrée une requête "query", en extrait les termes, enlève les
    stopwords et retourne la liste ordonnée des documents les plus pertinents 
    pour la recherche.
    
    AIDE: pour retourner les documents pertinents, il faut récupérer, pour 
    chaque terme, la liste des documents dans lesquels apparait chaque terme
    (utiliser l'index inversé). On ordonnera ensuite les documents par ordre 
    décroissant du nombre de termes de la requête qu'il contient.
    On ne retourne que les documents ayant au moins 1 terme de la requête

    Parameters
    ----------
    query : string
        la requête (à récupérer dans la dataframe préparé depuis le fichier query)
    inversed_index : dictionnary
        Index inversé terme => documents
    stopwords: list/dictionanry
        liste des stopwords à éliminer

    Returns
    -------
    sorted_doc_list : list
        liste des ids de documents ordonnés par pertinence

    """
    sorted_doc_list = None
    return sorted_doc_list

def precision_at_k(sorted_doc_list,expected_doc_list,k):
    """
    
    Calcule la précision au rang k pour les résultats d'une recherche 
    (fonction search_one_query) pour une liste de résultats attendus 
    (expected_doc_list) et retourne ce résultat dans un dictionnaire avec la
    précision et le rang k

    Parameters
    ----------
    sorted_doc_list : list
        liste des ids de documents ordonnés par pertinence
    expected_doc_list : list
        liste des ids des documents attendus pour cette requête 
    k : int
        rang auquel on calcule la précision

    Returns
    -------
    dictionnary
    Dictionnaire contenant la précision et le rang k

    """
    
    precision_at_k = {"precision": None, "k":None}
    return(precision_at_k)
    
    
def recall_at_k(sorted_doc_list,expected_doc_list,k):
    """
    
    Calcule le rappel au rang k pour les résultats d'une recherche 
    (fonction search_one_query) pour une liste de résultats attendus 
    (expected_doc_list) et retourne ce résultat dans un dictionnaire avec le
    rappel et le rang k

    Parameters
    ----------
    sorted_doc_list : list
        liste des ids de documents ordonnés par pertinence
    expected_doc_list : list
        liste des ids des documents attendus pour cette requête 
    k : int
        rang auquel on calcule le rappel

    Returns
    -------
    dictionnary
    Dictionnaire contenant le rappel et le rang k

    """
    
    recall_at_k = {"recall": None, "k": None}
    return(recall_at_k)


def average_precision(sorted_doc_list,expected_doc_list):
    """
    
    Calcule l'average precision pour les résultats d'une recherche 
    (fonction search_one_query) pour une liste de résultats attendus 
    (expected_doc_list) et retourne ce résultat

    Parameters
    ----------
    sorted_doc_list : list
        liste des ids de documents ordonnés par pertinence
    expected_doc_list : list
        liste des ids des documents attendus pour cette requête 

    Returns
    -------
    float
    average precision
    """
    
    AP = None
    return(AP)


def mean_average_precision(queries_df,eval_df,docs_index):
    """
    Calcule la mean Average precision sur l'ensemble des requêtes présente
    dans queries_df.
    
    AIDE : utiliser la fonction average_precision sur toutes les requetes de 
    queries_df

    Parameters
    ----------
    queries_df : pandas.DataFrame
        liste des requêtes.
    eval_df : pandas.DataFrame
        DESCRIPTION.
    docs_index : dictionnary
        index inversé terme => documents

    Returns
    -------
    Float
    La mean average precision pour toutes les requêtes d'évaluation

    """
    
    map_all = None
    return(map_all)
    
