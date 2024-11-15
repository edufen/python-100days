import random

# DIA 5

# ATIVIDADE 7 - BuzzFizz
def buzz_fizz():
    """
    Imprime os números de 1 a 100, substituindo múltiplos de 3 por "Buzz",
    múltiplos de 5 por "Fizz", e múltiplos de ambos por "BuzzFizz".
    """
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print("BuzzFizz")
        elif numero % 3 == 0:
            print("Buzz")
        elif numero % 5 == 0:
            print("Fizz")
        else:
            print(numero)

# PROJETO DIA 5 - Password Generator
def password_generator():
    """
    Gera uma senha aleatória baseada no número de letras, símbolos e números
    especificados pelo usuário.
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")

    try:
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input("How many symbols would you like?\n"))
        nr_numbers = int(input("How many numbers would you like?\n"))
    except ValueError:
        print("Please enter a valid number.")
        return

    password_list = []

    # Adiciona letras à senha
    for _ in range(nr_letters):
        password_list.append(random.choice(letters))

    # Adiciona símbolos à senha
    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))

    # Adiciona números à senha
    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))

    # Embaralha os caracteres
    random.shuffle(password_list)

    # Converte a lista em uma string
    password = "".join(password_list)

    print(f"Your password is: {password}")

# Main code para executar apenas o projeto
if __name__ == "__main__":
    # Descomente as atividades para testá-las
    # buzz_fizz()   # Descomente para rodar a atividade 7

    # Executando o Projeto Final (Password Generator)
    password_generator()
