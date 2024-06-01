import random
import xml.etree.ElementTree as ET
import unicodedata
import re

# Charger le fichier XML
tree = ET.parse('dictionnaire.xml')
root = tree.getroot()

# Initialiser une liste pour stocker les mots
liste_mots = []

# Parcourir chaque élément 'mot' dans la racine
for mot in root.findall('mot'):
    mot_valeur = mot.get('mot')  # Extraire la valeur de l'attribut 'mot'
    if mot_valeur:
        liste_mots.append(mot_valeur)

# Choisir un mot au hasard dans la liste 
mot_secret = random.choice(liste_mots)
essais_restants = 10
lettres_devinees = []
mot_affiche = [caractere if caractere == "-" else "_" for caractere in mot_secret]

def demander_une_lettre(lettres_devinees):
    # Boucle jusqu'à obtenir une lettre valide
    while True:
        lettre = input("Devinez une lettre : ").lower()
        if re.match("^[a-z]", lettre) and len(lettre) == 1:
            if lettre in lettres_devinees:
                print("Vous avez déjà deviné cette lettre.")
            else:
                return lettre
        elif len(lettre) == 0:
            print("Vous n'avez pas entré de lettre !")
        elif len(lettre) > 1:
            print("Veuillez entrer une seule lettre !")
        else:
            print("Veuillez entrer une lettre de l'alphabet !")
        
def enlever_accents(lettre):
    # Supprimer les accents des lettres
    return ''.join(
        c for c in unicodedata.normalize('NFD', lettre)
        if unicodedata.category(c) != 'Mn'
    )

def obtenir_potence(essais_restants):
    # Générer la potence en fonction des essais restants
    potence = [
        "  +---+",
        "  |   |",
        "      |",
        "      |",
        "      |",
        "      |",
        "========"
    ]
    
    if essais_restants < 10:
        potence[2] = "  O   |"  # Tête
    if essais_restants < 9:
        potence[3] = "  |   |"  # Tronc
    if essais_restants < 8:
        potence[3] = " /|   |"  # Bras gauche
    if essais_restants < 7:
        potence[3] = " /|\\  |"  # Bras droit
    if essais_restants < 6:
        potence[4] = " /    |"  # Jambe gauche
    if essais_restants < 5:
        potence[4] = " / \\  |"  # Jambe droite
    if essais_restants < 4:
        potence[5] = "  R   |"  # R
    if essais_restants < 3:
        potence[5] = "  RI  |"  # RI
    if essais_restants < 2:
        potence[5] = "  RIP |"  # RIP
    if essais_restants < 1:
        potence[5] = " RIP! |"  # RIP!
        
    return "\n".join(potence)

def afficher_etat_jeu(essais_restants, mot_affiche, lettres_devinees):
    # Afficher l'état actuel du jeu
    cadre_haut_bas = "~" * 60
    titre = "JEU DU PENDU".center(58)
    ligne_vide = "|                                                            |"
    ligne_essais = f"| Essais restants : {essais_restants:<40} |"
    ligne_mot = f"| Mot à deviner : {' '.join(mot_affiche):<42} |"
    ligne_lettres = f"| Lettres devinées : {' '.join(lettres_devinees):<39} |"
    potence = obtenir_potence(essais_restants).split("\n")
    potence_centre = [f"| {' ' * ((60 - len(ligne) - 2) // 2)}{ligne}{' ' * ((61 - len(ligne) - 2) // 2)} |" for ligne in potence]

    cadre = (
        f"+{cadre_haut_bas}+\n"
        f"| {titre} |\n"
        f"+{cadre_haut_bas}+\n"
        f"{ligne_vide}\n"
        f"{potence_centre[0]}\n"
        f"{potence_centre[1]}\n"
        f"{potence_centre[2]}\n"
        f"{potence_centre[3]}\n"
        f"{potence_centre[4]}\n"
        f"{potence_centre[5]}\n"
        f"{potence_centre[6]}\n"
        f"{ligne_vide}\n"
        f"{ligne_essais}\n"
        f"{ligne_mot}\n"
        f"{ligne_lettres}\n"
        f"{ligne_vide}\n"
        f"+{cadre_haut_bas}+"
    )
    
    print(cadre)

# Boucle principale du jeu
while essais_restants > 0 and "_" in mot_affiche:
    afficher_etat_jeu(essais_restants, mot_affiche, lettres_devinees)
    
    lettre = demander_une_lettre(lettres_devinees)
    lettre_sans_accent = enlever_accents(lettre)    
    lettre_trouvee = False

    lettres_devinees.append(lettre)
    
    for i, char in enumerate(mot_secret):
        if enlever_accents(char) == lettre_sans_accent:
            mot_affiche[i] = char
            lettre_trouvee = True

    if not lettre_trouvee:
        essais_restants -= 1

    print(" ")

# Afficher l'état final du jeu
afficher_etat_jeu(essais_restants, mot_affiche, lettres_devinees)
    
# Afficher le résultat du jeu
if "_" not in mot_affiche:
    print(f"\nFélicitations ! Vous avez deviné le mot : {mot_secret}.\n")
else:
    print(f"\nDommage ! Le mot était : {mot_secret}.\n")