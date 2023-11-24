import random

def play_game():
    choices = ['pedra', 'papel', 'tesoura']
    user_choice = input("Escolha pedra, papel ou tesoura: ").lower()
    computer_choice = random.choice(choices)

    print(f"Você escolheu: {user_choice}")
    print(f"O computador escolheu: {computer_choice}")

    if user_choice == computer_choice:
        print("Empate!")
    elif (user_choice == 'pedra' and computer_choice == 'tesoura') or \
         (user_choice == 'papel' and computer_choice == 'pedra') or \
         (user_choice == 'tesoura' and computer_choice == 'papel'):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

play_game()
