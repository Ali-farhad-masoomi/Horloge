import time

heure_actuelle = (0, 0, 0)  # Heure initiale

def afficher_heure(heure):
    print(f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}")

def regler_heure(nouvelle_heure):
    global heure_actuelle
    heure_actuelle = nouvelle_heure
    afficher_heure(heure_actuelle)

def regler_alarme(heure_alarme):
    while True:
        heure_actuelle = time.localtime(time.time())[3:6]
        if heure_actuelle == heure_alarme:
            print("Réveillez-vous ! L'alarme a sonné.")
            break
        time.sleep(1)

# Afficher l'heure actuelle toutes les secondes
try:
    while True:
        afficher_heure(heure_actuelle)
        time.sleep(1)
        heure_actuelle = time.localtime(time.time())[3:6]

except KeyboardInterrupt:
    print("\nProgramme arrêté par l'utilisateur.")
