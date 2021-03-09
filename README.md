# Evaluation sur un jeu de donn�es de moteur de recherche

## Ne pas utiliser scikit ou de librairies non standards. 
## Utilisez numpy et pandas.

## Enonc� :

* Cloner le d�p�t sur votre machine (le contenu compl�t� sera a envoyer par mail sous forme d'une archive)
* 1 - Compl�ter le code des sous fonctions des fichiers qui se trouvent dans src/main 
* 2 - Compl�ter et corriger le fichier search_and_eval.py � la racine
* 3 - V�rifier que tout s'execute bien et que les print demand�s s'affichent bien
* 4 - Faire une pip freeze > requirements.txt pour que l'on puisse installer les librairies que vous utilisez

## Pour soumettre 
* PAS DE COMMIT/PUSH
* Zippez votre projet et envoyez le par mail.


## RAPPELS DES METRIQUES

* Rappel@k= nombre de documents pertinents retourn�s dans les k premiers / nombre de docs pertinents pour la requ�te
* Pr�cision@k = nombre de documents pertinents retourn�s dans les k premiers / k
* Average precision: Pour une requ�te, pour i=1 � N(nombre de documents pertinents pour la requ�te), moyenne des pr�cisions@1, pr�cisions@2....pr�cisions@N
* Mean average precision: Moyenne de toutes les Average pr�cision pour toutes les requ�te.