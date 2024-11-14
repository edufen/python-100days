import random

# DIA 4

# Função do jogo Pedra, Papel e Tesoura
def rock_paper_scissors():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    # Lista com as imagens das opções
    game_images = [rock, paper, scissors]

    # Entrada do usuário
    try:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
        if user_choice < 0 or user_choice >= 3:
            print("You typed an invalid number, you lose!")
            return
    except ValueError:
        print("Invalid input! Please enter a number (0, 1, or 2).")
        return

    print("Your choice:")
    print(game_images[user_choice])

    # Escolha do computador
    computer_choice = random.randint(0, 2)
    print("Computer's choice:")
    print(game_images[computer_choice])

    # Lógica para determinar o vencedor
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")

# Main code para executar apenas o projeto final
if __name__ == "__main__":
    # Descomente as atividades para testá-las
    # atividade_1()   # Descomente para rodar a atividade 1
    # atividade_2()   # Descomente para rodar a atividade 2
    # atividade_3()   # Descomente para rodar a atividade 3

    # Executando o Projeto Final (Rock, Paper, Scissors)
    rock_paper_scissors()
