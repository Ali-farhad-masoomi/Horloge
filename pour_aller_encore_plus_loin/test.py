import time
import threading

class Horloge:
    def __init__(self):
        self.pausee = False
        self.temps_actuel = 0
        self.thread = threading.Thread(target=self.actualiser_heure)

    def actualiser_heure(self):
        while not self.pausee:
            self.temps_actuel = time.time()
            print("Heure actuelle:", time.ctime(self.temps_actuel))
            time.sleep(1)

    def mettre_en_pause(self):
        self.pausee = True

    def relancer(self):
        self.pausee = False

print("Le programme est en pause. Appuyez sur Entrée pour continuer...")
input()  # Cette ligne met le programme en pause jusqu'à ce que l'utilisateur appuie sur Entrée
# Exemple d'utilisation

horloge = Horloge()

# Démarrez l'actualisation de l'heure dans un thread
horloge.thread.start()

# Attendez que le thread se termine
horloge.thread.join()


print("Le programme a repris son exécution.")

