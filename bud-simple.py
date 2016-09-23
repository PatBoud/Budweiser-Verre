# Code pour demontrer l'utilisation du verre lumiere de but Budweiser
# Par: PatBoud
# Date: 2016-09-22
from time import sleep

# Importation de la classe Verre
from budverre import verre


# Initialisation des verres
# verreX = verre("NomDuVerre", "Adresse_MAC")
# Remplacez l'adresse MAC par celle de votre verre
# Voir dans le fichier "budverre.py" pour de l'aide

verrePat = verre("Pat", "44:BF:E3:08:44:5A")
verreRach = verre("Rachou", "44:BF:E3:06:A3:E9")

# On pourrait aussi utiliser un tableau des verres, par exemple:
# 



# Attente de 3 secondes
sleep(3)

# On fait clignoter un premier verre
verrePat.but()

# Attente de 15 secondes pour lui laisser le temps de finir de clignoter
sleep(15)

# On fait clignoter un deuxieme verre
verreRach.but()

# Attente de 15 secondes pour lui laisser le temps de finir de clignoter
sleep(15)

# Deconnexion des verres. Important pour qu'ils redeviennent disponibles pour connexion
# par un autre programme ou l'application mobile. Sans cela, le verre redevient disponible
# apres 10 minutes, ou en enlevant les piles
verrePat.disconnect()
verreRach.disconnect()
