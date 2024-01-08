import time

heure_actuelle = (0, 0, 0)  # Heure initiale
format_24h = True  # Mode 24 heures par défaut

def afficher_heure(heure, format_24h):
    if format_24h:
        print(f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}")
    else:
        am_pm = "AM" if heure[0] < 12 else "PM"
        heure_12h = heure[0] if heure[0] <= 12 else heure[0] - 12
        heure_12h = 12 if heure_12h == 0 else heure_12h
        print(f"{heure_12h:02d}:{heure[1]:02d}:{heure[2]:02d} {am_pm}")

def regler_heure(nouvelle_heure):
    global heure_actuelle
    heure_actuelle = nouvelle_heure
    afficher_heure(heure_actuelle, format_24h)

def regler_alarme(heure_alarme):
    while True:
        heure_actuelle = time.localtime(time.time())[3:6]
        if heure_actuelle == heure_alarme:
            print("Réveillez-vous ! L'alarme a sonné.")
            break
        time.sleep(1)

def choisir_format_affichage():
    global format_24h
    choix = input("Choisissez le format d'affichage (12h ou 24h) : ").lower()
    format_24h = choix == "24h"

# Afficher l'heure actuelle toutes les secondes
try:
    while True:
        afficher_heure(heure_actuelle, format_24h)
        time.sleep(1)
        heure_actuelle = time.localtime(time.time())[3:6]

except KeyboardInterrupt:
    print("\nProgramme arrêté par l'utilisateur.")
import time

heure_actuelle = (0, 0, 0)  # Heure initiale
format_24h = True  # Mode 24 heures par défaut

def afficher_heure(heure, format_24h):
    if format_24h:
        print(f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}")
    else:
        am_pm = "AM" if heure[0] < 12 else "PM"
        heure_12h = heure[0] % 12
        heure_12h = 12 if heure_12h == 0 else heure_12h
        print(f"{heure_12h:02d}:{heure[1]:02d}:{heure[2]:02d} {am_pm}")

def regler_heure(nouvelle_heure):
    global heure_actuelle
    heure_actuelle = nouvelle_heure
    afficher_heure(heure_actuelle, format_24h)

def regler_alarme(heure_alarme):
    while True:
        heure_actuelle = time.localtime(time.time())[3:6]
        if heure_actuelle == heure_alarme:
            print("Réveillez-vous ! L'alarme a sonné.")
            break
        time.sleep(1)

def choisir_format_affichage():
    global format_24h
    choix = input("Choisissez le format d'affichage (12h ou 24h) : ").lower()
    format_24h = choix == "24h"

# Afficher l'heure actuelle toutes les secondes
try:
    choisir_format_affichage()  # Demander le format d'affichage au début
    while True:
        afficher_heure(heure_actuelle, format_24h)
        time.sleep(1)
        heure_actuelle = time.localtime(time.time())[3:6]

except KeyboardInterrupt:
    print("\nProgramme arrêté par l'utilisateur.")
