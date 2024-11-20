# DIA 7

# PROJETO DIA 7 - Jogo da Forca (Hangman Game)

import random
import unicodedata

# Função para normalizar strings (remover acentos e transformar em minúsculas)
def normalize_string(s):
    s = s.lower()
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

# Lista de palavras organizada em ordem alfabética
word_list = [
    "abelha", "besouro", "bicho-preguiça", "cabra", "cachorro",
    "canguru", "cavalo", "cavalo-marinho", "cervo", "chacal",
    "chimpanzé", "coruja", "corvo", "coyote", "dingo", "elefante",
    "foca", "furão", "galo", "gato", "girafa", "golfinho",
    "hamster", "iguana", "jacaré", "jaguatirica", "lagarto",
    "leão", "leopardo", "lêmure", "lontra", "ovelha", "panda",
    "papagaio", "pássaro", "peixe", "pinguim", "porco-espinho",
    "porquinho-da-índia", "puma", "raposa", "rato", "rena",
    "serpente", "tartaruga", "tigre", "tubarão", "urso",
    "urso-polar", "zebra"
]

# Normaliza a lista de palavras
normalized_word_list = [normalize_string(word) for word in word_list]

# Arte ASCII para as etapas do jogo
stages = [
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
]

# Função para revelar letras aleatórias
def reveal_letters(word, display):
    indices = [i for i, letter in enumerate(word) if display[i] == "_"]

    if len(indices) > 0:
        # Verifica a quantidade de letras que faltam
        missing_letters = len(indices)

        if missing_letters <= 2:
            reveal_count = 1  # Revela 1 letra se faltar 1 ou 2 letras
        elif len(word) > 8:
            reveal_count = 2  # Revela 2 letras se a palavra tiver mais de 8 letras
        else:
            reveal_count = 1  # Revela 1 letra se a palavra tiver 7 ou 8 letras

        for _ in range(reveal_count):
            index_to_reveal = random.choice(indices)
            display[index_to_reveal] = word[index_to_reveal]
            indices.remove(index_to_reveal)

# Função principal do jogo
def play_game():
    chosen_word = random.choice(word_list)
    normalized_chosen_word = normalize_string(chosen_word)
    display = ["_"] * len(chosen_word)
    lives = 7
    word_attempts = 2
    guessed_letters = []  # Letras já tentadas
    guessed_words = []  # Palavras já tentadas
    # revealed_once = False  # Não está funcionando, a ideia era revelar letras apenas uma vez.
    while True:
        # Exibe o estágio atual do jogo
        print(stages[6 - lives])
        print(f"Você tem: {lives} vidas restantes.")
        print(" ".join(display))  # Mostra o progresso atual
        print(f"Letras tentadas: {', '.join(guessed_letters)}")  # Mostra letras já tentadas
        print(f"Palavras tentadas: {', '.join(guessed_words)}")  # Mostra palavras já tentadas

        # Verifica se deve revelar letras
        if lives <= 2:
            reveal_letters(chosen_word, display)

        # Solicita ao jogador adivinhar
        guess = input("Adivinhe uma letra ou a palavra: ").lower()

        if len(guess) == 1:  # Adivinhando uma letra
            if guess in guessed_letters:
                print("Você já tentou essa letra. Tente outra.")
                continue

            guessed_letters.append(guess)  # Adiciona a letra tentada

            # Verifica se o palpite está na palavra
            if guess in normalized_chosen_word:
                # Atualiza a lista 'display' para revelar letras corretas
                for index, letter in enumerate(normalized_chosen_word):
                    if letter == guess:
                        display[index] = chosen_word[index]
            else:
                # Reduz uma vida caso o palpite esteja errado
                lives -= 1
                print(f"Palpite errado! Você perdeu uma vida.")

        elif len(guess) > 1:  # Adivinhando a palavra inteira
            if word_attempts > 0:
                if normalize_string(guess) == normalized_chosen_word:
                    print(f"Parabéns! Você adivinhou a palavra '{chosen_word}' e venceu!")
                    break
                else:
                    word_attempts -= 1
                    lives -= 3  # Perde 3 vidas ao errar a palavra inteira
                    guessed_words.append(guess)  # Adiciona a palavra tentada
                    print(f"Palpite errado! Você perdeu 3 vidas. Restam {word_attempts} tentativas de palavra.")
            else:
                print("Você já usou todas as suas tentativas para adivinhar a palavra.")
        else:
            print("Escolha inválida. Tente novamente.")
            continue

        # Verifica condições de vitória ou derrota
        if "_" not in display:
            print(f"Parabéns! Você completou a palavra '{chosen_word}' e venceu!")
            break
        if lives <= 0:
            print(stages[0])  # Mostra o último estágio
            print(f"Você perdeu! A palavra era '{chosen_word}'.")
            break

# Main code para executar apenas o projeto
if __name__ == "__main__":
    # Não há atividades neste dia, apenas o projeto.

    # Loop para jogar novamente
    while True:
        play_game()
        play_again = input("Deseja jogar novamente? (y/n): ").lower()
        if play_again != 'y':
            break
    print("Obrigado por jogar! Até a próxima 🐺.")