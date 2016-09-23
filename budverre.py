# ============================================================
# Bud-Verre - Controleur de Verres Lumiere de but Budweiser
# Par: PatBoud
# Date: 2016-09-22
#
# Vous permet de faire clignoter des verres lumiere de but Budweiser a volonte.
#
# Materiel:
# - RaspberryPi 3 (avec Bluetooth 4.0 integre)
#
# Prerequis Linux:
# - BlueZ : pour utiliser le Bluetooth
#
# Librairies Python:
# - pexpect : pour utiliser les outils de ligne de commande
#   https://pexpect.readthedocs.io/en/stable/install.html
#
#
# Information requise sur les verres:
#
# MAC Address: On peut l'obtenir, depuis le systeme linux, en
# executant la commande "sudo hcitool lescan"
# ============================================================

from time import sleep
import pexpect

# Classe Verre
class verre:
	#Constructeur
	def __init__(self, nom, mac):
		self.nom = nom
		self.mac = mac
		#Connexion automatique
		self.connect()

	#Connexion
	def connect(self):
		# On execute gatttool en mode interactif.
		self.gatt = pexpect.spawn('gatttool -I')

		# Connexion au verre
		print ("Connexion au verre " + self.nom + " (" + self.mac + ") ...")
		self.gatt.sendline('connect {0}'.format(self.mac))
		self.gatt.expect('Connection successful')
		print ("Connexion au verre " + self.nom + " : OK")

		#Handshake
		self.gatt.sendline("char-write-req 0x0036 0100")
		self.gatt.sendline("char-write-req 0x003b 550106" + self.mac.replace(":", ""))
		self.gatt.sendline("char-write-req 0x003b 62550106bc0a")
		sleep(1)

	#But!
	def but(self):
		self.gatt.sendline("char-write-req 0x003b 625510c7")

	#Deconnexion
	def disconnect (self):
		print ("Deconnexion du verre " + self.nom + " ...")
		self.gatt.sendline("char-write-req 0x003b 625520d7")
		sleep(1)
		self.gatt.sendline('disconnect')
		print ("Deconnexion du verre " + self.nom + " : OK")
