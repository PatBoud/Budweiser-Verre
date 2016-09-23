# ============================================================
# Bud-Party - Controleur de Verres Lumiere de but Budweiser
# Par: PatBoud
# Date: 2016-09-22
#
# Vous permet de faire clignoter vos verres lumiere de but Budweiser au hasard
# pour toute la soiree! PARTY!
#
# ============================================================

from random import randint
from time import sleep
from budverre import verre

# Liste des verres
mesVerres = []

# Delais min et max entre les "buts"., en secondes
delaisMin = 300  # 300 secondes = 5 minutes
delaisMax = 900  # 900 secondes = 15 minutes

try:
	print("- DEBUT DU PARTY -")
	print("Appuyez sur CTRL + C pour quitter...")
	print("")
	sleep(1)

	#Initialisation des verres
	print("- CONNEXION AUX VERRES -")
	# Remplacerz ici le nom et l'adresse MAC de vos verres
	mesVerres.append(verre("Pat", "44:BF:E3:08:44:5A"))
	mesVerres.append(verre("Rachou", "44:BF:E3:06:A3:E9"))

	while True:
		# Un delais au hasard entre 5 et 15 minutes
		nbSecondes = randint(delaisMin, delaisMax)
		print "Secondes d'attente: " + str(nbSecondes)
		sleep(nbSecondes)

		# On boucle dans la liste des verres pour tous les faire clignoter
		print ("Et c'est le buuuuuuuut!")
		for index in range(len(mesVerres)):
			mesVerres[index].but()

except:
	#Deconnexion des verres
	print("")
	print("- DECONNEXION DES VERRES -")
	for index in range(len(mesVerres)):
		mesVerres[index].disconnect()

	print ("- FIN DU PARTY -")
