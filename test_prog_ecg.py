def classify_heart_rate(bpm):
    """
    Classe le rythme cardiaque en fonction des normes de fréquence.
    
    :param bpm: Battements par minute mesurés.
    :return: Classification du rythme cardiaque.
    """
    if bpm < 60:
        return "Bradycardie (Rythme lent)"
    elif 60 <= bpm <= 100:
        return "Rythme normal"
    elif 100 < bpm <= 120:
        return "Tachycardie légère"
    elif 120 < bpm <= 140:
        return "Tachycardie modérée"
    else:
        return "Tachycardie sévère"

def get_user_input():
    """
    Demande à l'utilisateur de saisir la fréquence cardiaque en bpm.
    
    :return: Fréquence cardiaque saisie par l'utilisateur.
    """
    while True:
        try:
            # Demande de l'entrée utilisateur
            bpm = float(input("Veuillez entrer le rythme cardiaque (en bpm) : "))
            if bpm <= 0:
                print("Veuillez entrer une valeur positive.")
                continue
            return bpm
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")

# Appel des fonctions
heart_rate = get_user_input()  # Récupère la saisie de l'utilisateur
classification = classify_heart_rate(heart_rate)  # Classifie le rythme cardiaque
print(f"Rythme cardiaque : {heart_rate} bpm - {classification}")  # Affiche le résultat
