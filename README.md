# Access-et-recherche-d-informations

## TP1

### tokenize_cacm.py

#### GetTokens

Description :

Prends un texte. Passe tous ses mots en minuscule. Récupère uniquement les vrais mots et les tokenize. Créer un fichier du même nom de l'ancien avec l'extension .tok. Écris un mot par ligne.

Input :

@param le dossier avec les fichiers

### zipf.py

Description :
Parcours les fichiers et récupére les mots. Inscrit leurs nombre d'occurence dans un dictionnaire. Inscrit les n résultats les plus fréquents dans resultat.txt. Inscrit le nombre total de mots dans resultat.txt

Input :
@param le dossier avec les fichiers
@param le nombre de mots à écrire dans le fichier

## TP2

### AntiDico

Description :
On récupère l'anti -dictionnaire. Pour tous les fichiers, on récupère leurs contenue. Si le mot est pas dans l'anti-dictionnaire, on l'écris  et le tronque avec la troncature de porter.

Input :
@param dossier avec nos mots
@param chemin de l'antidictionnaire
@param le lien pour la destination de l'écriture

### Vocabulary

Description :
Parcours des documents qu'on récupère dans un dictionnaire. Dans un dictionnaire global à la fonction, on y indique le nombre d'occurrence de ce mot sur l'ensemble des documents. On calcule l'idf_i pour ses mots et on les sauvegarde dans le document vocabulaire.json

Input :
@param la source du fichier
@param la destination d'écriture

### DicoWithOccurence

Description :
On parcourt les fichiers et récupère la tf.

Input :
@param la source du fichier
@param la destination d'écriture

### Ponderation

Description :
Parcours des fichiers. On charge leur contenu et celui du vocabulaire. Pour chacun des mots, on calcule la tf_idf et l'inscrit dans le fichier de destination

Input :
@param source des fichiers
@param source du vocabulaire
@param destination du résultat

### Norme

Description :
Pour tous les fichiers on récupère le contenu. Pour tous ses fichiers, on calcule sa norme et on la sauvegarde.

Input :
@param source du fichier
@param destination du résultat

## TP3

### Loads

Description :
Créer un tableau de deux dimensions. Premier indice filename et deuxième le contenue renvoyé par la fonction load de tous les fichiers d'un dossier

Input:
@param le dossier avec les fichiers

### Load

Description :
Récupère et envoie le contenue d'un fichier

Input :
@param le lien du fichier

### Main

Description :
On charge notre index_inversé, le vocabulaire et les normes.
Dans une boucle infinie, on demande la requête. Si requête de sortie, on sort du programme. On prépare notre matériel. On récupère la tf de la requête. On fait la norme de la requête puis la tf_idf. On trie en décroisant et enfin, on affiche notre résultat.