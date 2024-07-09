def afficher_table_multiplication():
    """Affiche la table de multiplication pour un nombre donné, de min à max."""
    try:
        n = int(input("Donner le nombre pour lequel vous voulez afficher la table de multiplication : "))
        min_val = int(input(f"Donner par quel nombre commence la table de multiplication de {n} : "))
        max_val = int(input(f"Donner le dernier nombre de la multiplication de {n} : "))
    except ValueError:
        print("ERREUR: Veuillez entrer des nombres entiers valides.")
        return

    if min_val >= max_val:
        print("ERREUR: Le minimum doit être strictement inférieur au maximum.")
    else:
        for i in range(min_val, max_val + 1):
            resultat = i * n
            print(f"{i} * {n} = {resultat}")

if __name__ == "__main__":
    afficher_table_multiplication()
