
# Introduction
Cet outil permet de tester le eida-Fedrator de facon automatique et  de comparer les resultats du eida-Fedrator à un noeud.
Le code est adapté de l'outil WS-RESIF (developpé à RESIF).

# Requirements
* Python 3
* requests==2.19.1 pour réaliser les requettes
* colorama==0.3.9 pour colorer les messages en sortie

# Architecture
* WSEIDAtest:  le script pour exécuter les tests 
* TESTS_dataselect.py : la liste des tests dataselect
* TESTS_station.py : la liste des tests station
* config.py : contient les acces sur les données restreins (à ignorer)
* utils: Variables globales.

# Installation
* sudo pip3 install -r requirements.txt
* Pour définir les tests éditer les fichiers suivants "TESTS_dataselect.py" et "TESTS_station.py".

# Fonctionnement

### Fonctionnement general

Il existe deux types de tests dataselect et station ; Vous devez renseigner les requêtes à tester dans les fichiers : TESTS_dataselect, et TESTS_station. 
Pour choisir le type de test vous pouvez selectionner les options --station et --dataselect 

Le script va par défaut passer les tests uniquement sur le eida-federator. Il est possible de choisir d'autres noeuds avec l'option --nodes. Lorsque que cette option est utilisé une comparaison des resultats au format text est réalisée entre eida-Fedrator et le(s) noeud(s).

Les tests sur le federator peuvent être désactivés avec --noeida dans ce cas il faut indiquer un noeud minimun.

Pour exécuter un test précis il faut indiquer l'ID du test avec l'option --idcontains. 



### Configuration des fichiers tests 

  Une variable TESTS est a déclaré dans les fichiers : TESTS_dataselect et TESTS_station avec le fomat ci-dessous:

    TESTS = [

     	 {

     		'id': 'la description du test, c'est cette valeur qui sera utiliser pour l'argument --idcontains ',

     		'get': ' la requete à tester sans le domaine de noeud. Ce-si seras ajouter automatqiuement',

     		'test': 'peut contenir IN** ou ==**. Ce test est utilisé pour comparer les resultat en formats text'. 
      }

     ]

  **La comparaison des resultas ce fait UNIQUEMENT sur le format text. 
  'in' vérifie si le resulat du noeud X est dans le resulat du eida-federator. 
  '==' Compare si les resultas sont identiques.

  Des exemples sont disponibles dans TESTS_dataselect-dist.py et TESTS_station_dist.py.

# Utilisation 
    usage: WSEIDAtest.py [-h] [--dump] [--dataselect] [--station] [--noeida]

                     [--nodes STR] [--idcontains STR]
                     

    optional arguments:
      -h, --help        show this help message and exit

      --dump            dump HTTP response to disk

      --size            Calculate the size


      --dataselect      dataselect tests

      --station         station tests

      --noeida          no tests on EIDA-Federator

      --nodes STR       Nodes or 'ALL'

      --idcontains STR  only run tests with id containing <STR> string



# OUTPUT
Vous retrouverez la requête testée, la durée d'exécution, la taille de fichier et le résultat de la comparison* (avec --nodes). 

# Exemples

   WSEIDAtest.py --nodes RESIF 
   Réalise tous les tests (dataselect et station) sur eida-federator et RESIF.

   WSEIDAtest --dataselact --noeida --nodes RESIF,GFZ
   Réalise tous les tests dataselect sur RESIF et GFZ et pas sur eida-federator.







