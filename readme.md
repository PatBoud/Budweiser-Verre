# Bud-Verre : Controleur de Verres Lumiere de but Budweiser

PatBoud - 2016-09-22

Vous permet de faire clignoter des verres lumiere de but Budweiser a volonte.

## Materiel:
- RaspberryPi 3 (avec Bluetooth 4.0 integre)

## Prerequis Linux:
- BlueZ : pour utiliser le Bluetooth

## Librairies Python:
- pexpect : pour utiliser les outils Bluetooth en ligne de commande
  https://pexpect.readthedocs.io/en/stable/install.html

## Information requise sur les verres:
- MAC Address: On peut l'obtenir, depuis le systeme linux, en executant la commande "sudo hcitool lescan"


## To-Do
- Faire gerer la liste de verres par la librairie
    - Ajouter une methode .random() pour faire clignoter un verre au hasard
