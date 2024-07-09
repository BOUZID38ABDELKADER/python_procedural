def convertir():
    choix = input(
        "Que voulez-vous convertir ? :\n\n"
        "Tapez 1 si vous voulez convertir le centimètre en pouce\n"
        "Tapez 2 si vous voulez convertir le pouce en centimètre\n"
    )

    if choix == '1':
        print("Vous avez choisi de convertir le centimètre en pouce.\n")
        centimetres = input("Donnez la valeur en centimètres à convertir : \n")
        try:
            centimetres = float(centimetres)
            pouces = centimetres * 0.394
            print(f"Le résultat est : {centimetres} centimètres = {pouces:.2f} pouces")
        except ValueError:
            print("Veuillez entrer une valeur numérique valide.")
        return 1

    elif choix == '2':
        print("Vous avez choisi de convertir le pouce en centimètre.\n")
        pouces = input("Donnez la valeur en pouces à convertir : \n")
        try:
            pouces = float(pouces)
            centimetres = pouces * 2.54
            print(f"Le résultat est : {pouces} pouces = {centimetres:.2f} centimètres")
        except ValueError:
            print("Veuillez entrer une valeur numérique valide.")
        return 1

    else:
        print("Merci de bien choisir 1 ou 2 selon les choix proposés ci-dessus !")
        return 0

def main():
    while True:
        if convertir() == 1:
            break

if __name__ == "__main__":
    main()
