# Evaluation sur un jeu de données de moteur de recherche

## Ne pas utiliser scikit ou de librairies non standards. 
## Utilisez numpy et pandas.

## Enoncé :

* Cloner le dépôt sur votre machine (le contenu complété sera a envoyer par mail sous forme d'une archive)
* 1 - Compléter le code des sous fonctions des fichiers qui se trouvent dans src/main 
* 2 - Compléter et corriger le fichier search_and_eval.py à la racine
* 3 - Vérifier que tout s'execute bien et que les print demandés s'affichent bien
* 4 - Faire une pip freeze > requirements.txt pour que l'on puisse installer les librairies que vous utilisez

## Pour soumettre 
* PAS DE COMMIT/PUSH
* Zippez votre projet et envoyez le par mail.


## RAPPELS DES METRIQUES

* Rappel@k= nombre de documents pertinents retournés dans les k premiers / nombre de docs pertinents pour la requête
* Précision@k = nombre de documents pertinents retournés dans les k premiers / k
* Average precision: Pour une requête, pour i=1 à N(nombre de documents pertinents pour la requête), moyenne des précisions@1, précisions@2....précisions@N
* Mean average precision: Moyenne de toutes les Average précision pour toutes les requête.