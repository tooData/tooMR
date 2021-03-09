#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Ajouter les imports nécessaires. 
"""

def load_evaluation_db(file_path):
    """
    Prend en entrée le chemin relatif du fichier (qrels.txt) contenant les paires
    "requete - nième document pertinent" et retourne un dataframe
    avec ces colonnes et une troisième donnant le rang de pertinence du document 
    pour la requête. Première ligne du doc pour la requête = rang 1, deuxième ligne
    du doc pour la requête = rang 2
    
    
    AIDE: Utiliser un chargement avec pandas et la fonction rank et groupby de
    pandas pour les rangs. on ignore les deux dernières colonnes à 0 du fichier qrels.txt
    
    Parameters
    ----------
    file_path : string
        Chemin relatif du fichier dans le projet (qrels.txt)

    Returns
    -------
    eval_df : pandas.DataFrame
        Dataframe avec trois colonnes id_query;id_document;pertinence_rank

    """
    eval_df = None
    
    return (eval_df)


def load_queries(filepath):
    """
    Prend entrée le chemin relatif du fichier (query.txt) contenant le texte 
    des requêtes et retourne un dataframe pandas avec 2 colonnes, une étant l'id
    de la requête, (.I dans le fichier) et l'autre .W qui est la requête elle meme.
    
    AIDE: Le format n'est pas standard. Il s'agit d'un stockage en ligne avec
    l'entête sous forme .I .W .N. il faut parcourir le fichier ligne par ligne 
    et construire le dataframe.
    
    Parameters
    ----------
    file_path : string
        Chemin relatif du fichier dans le projet (query.txt)

    Returns
    -------
    eval_df : pandas.DataFrame
        Dataframe avec deux colonnes id_query;query_txt

    """
    queries_df = None
    
    return (queries_df)


def load_documents(filepath):
    """
    Prend entrée le chemin relatif du fichier (cacm.all) contenant le texte 
    des documents qui vont être la base dans laquelle cherche les requêtes.
    Retourne un dataframe avec 4 colonnes contenant l'id  du document (.I), le titre
    du document (.T), ses auteurs (.A) et la conférence (.B)
    
    AIDE: Le format n'est pas standard. Il s'agit d'un stockage en ligne avec
    l'entête sous forme .I .T .B .A .N .X qui contiennt les infos du document.
    Il faut parcourir le fichier ligne par ligne et construire le dataframe.
    
    Parameters
    ----------
    file_path : string
        Chemin relatif du fichier dans le projet (cacm.all)

    Returns
    -------
    eval_df : pandas.DataFrame
        Dataframe avec 4 colonnes id_doc;title_doc;authors_doc;conf_doc

    """
    docs_df = None
    
    return (docs_df)

def load_stopwords(filepath):
    """
    Prend entrée le chemin relatif du fichier (common_words) contenant les mots
    communs qu'il faut retirer des requêtes et des documents car ils ne sont pas
    discriminants.
    
    AIDE: On va stocker ces mots dans une liste pour un accès simplifier. Vous 
    pouvez aussi les stocker dans une hashmap/dictionnaire pour un accès simple
    ET rapide. A votre préférence
    
    Parameters
    ----------
    file_path : string
        Chemin relatif du fichier dans le projet (common_words)

    Returns
    -------
    stopwords : list OR dictionnary
        liste des mots à exclure des documents et requêtes.

    """
    stopwords = None
    
    return (stopwords)





