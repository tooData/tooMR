#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ajouter les imports nécessaires des modules que vous avez complété.

"""

if __name__ == "__main__": 
    
    #Préparation des données et de l'index
    #corrigez les 5 lignes pour bien importer les fonctions
    eval_df = load_evaluation_db(eval_filepath)
    queries_df = load_queries(queries_filepath)
    docs_df = load_documents(docs_filepath)
    stopwords = load_stopwords(stopwords_filepath)
    docs_index = index_documents(docs_df,stopwords)
    
    #tests    
    """
    Sortir les résultats pour 10 requêtes au hasard 
    
    """
    #votre code ici. Printez les requêtes et le titre des documents retournés
    #utilisez la fonction search_one_query du module search.py
    
    
    """ 
    Sortir le rappel@3 et précision@3 pour 10 requêtes au hasard depuis 
    """
    #votre cote ici. Printez les requête, leur rappel @ 3 et leur précision @ 3
    #utilisez la fonction recall_at_k et precision_at_k du module search.py
    
    
    """ 
    Sortir l'average precision pour 10 requêtes au hasard depuis 
    """
    #votre cote ici. Printez les requête, et leur average precision
    #utilisez la fonction average_precision du module search.py
    
    """
    Calculer la mean average precision sur toutes les requêtes de queries_df
    """
    #corrigez la ligne pour bien importer les fonctions
    map_all = mean_average_precision(queries_df,eval_df,docs_index)
    print(map)