import os
import random
import time

def clear_screen():
    """Efface l'écran en fonction du système d'exploitation."""
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def generate_sequence(length=4):
    """Génère une séquence aléatoire de chiffres de la longueur spécifiée."""
    return ''.join(str(random.randint(0, 9)) for _ in range(length))

def main():
    score = 0
    sequence = generate_sequence()

    while True:
        print("Retenez la séquence :")
        print(sequence)
        time.sleep(4)
        clear_screen()
        
        user_input = input("Donnez la séquence : ")
        
        if user_input == sequence:
            sequence += str(random.randint(0, 9))
            score += 1
        else:
            break

    print(f"Réponse incorrecte, la séquence était : {sequence}, votre score est : {score}")

if __name__ == "__main__":
    main()
