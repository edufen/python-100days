# DIA 3

# ATIVIDADE 5 - BMI Calculator with Interpretations

# Função que calcula o BMI (Índice de Massa Corporal) e retorna a interpretação.
def bmi_calculator(weight, height):
    # Calcula o BMI
    bmi = weight / (height ** 2)

    # Interpreta o BMI
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    else:
        return "Overweight"  # Caso para sobrepeso.

# Exemplo de uso da função
def run_bmi_calculator():
    weight = 85
    height = 1.85
    result = bmi_calculator(weight, height)
    # Exibindo o resultado calculado
    print(f"BMI: {weight / (height ** 2):.2f} - {result}")

# ATIVIDADE 6 - Pizza Order

# Função que calcula o preço final do pedido de pizza
def pizza_order():
    # Mensagem de boas-vindas
    welcome = "Welcome to Python Pizza Deliveries!"
    print(welcome)

    # Exibe os preços das pizzas
    print("Small Pizza: $15")
    print("Medium Pizza: $20")
    print("Large Pizza: $25")

    # Pergunta ao usuário qual tamanho de pizza ele quer
    size = input("What size pizza would you like? (small, medium, large): ").lower()

    # Definindo o preço base dependendo do tamanho escolhido
    if size == "small":
        price = 15
    elif size == "medium":
        price = 20
    elif size == "large":
        price = 25
    else:
        print("Invalid size. Please choose 'small', 'medium', or 'large'.")
        return

    # Pergunta se o usuário quer adicionar pepperoni
    pepperoni = input("Do you want to add pepperoni? (yes/no): ").lower()
    if pepperoni == "yes":
        if size == "small":
            price += 2
        else:
            price += 3

    # Pergunta se o usuário quer adicionar queijo extra
    cheese = input("Do you want to add extra cheese? (yes/no): ").lower()
    if cheese == "yes":
        price += 1

    # Exibe o preço final
    print(f"Your final bill is: ${price}")

# PROJETO DIA 3 - Treasure Island Project (Wolf Hunt Version)

def wolf_hunt():
    # Introdução ao projeto
    print(''' 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣶⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⠿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣯⣥⣤⣄⢸⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⢿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠘⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠻⣿⣧⠀⢻⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠙⠉⠀⠀⠀⠀⢱⣆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⡿⠋⠀⣼⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⢿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⠋⠀⢀⣤⣿⣿⣿⣿⣿⣿⠋⠁⠀⢀⣀⡀⠀⠉⠛⢿⣿⣦⡀⠀⠀⠀⢀⣴⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣟⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⠃⢠⣼⣿⣿⣿⣿⣿⣷⣦⣤⣀⡀⠁⠀⢀⣴⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢠⣿⠋⠁⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠸⠇⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⣸⣿⣿⣿⠟⠛⠉⣁⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣠⠖⠋⠁⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡞⠁⣸⠿⠛⠁⢠⣴⣾⡟⠁⠀⣴⣿⣿⣿⡿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣾⣿⠀⠀⠁⢀⣴⣾⣿⣿⡿⠁⠀⣸⣿⣿⡿⠋⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⠋⠀⠀⢹⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣤⣶⣶⣾⣿⣿⣿⣿⣿⡄⣠⣴⣿⣿⣿⣿⣿⡇⠀⢰⣿⣿⣿⠁⠀⡿⠟⠋⠉⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⣀⠀⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀
⠀⢀⣠⣶⣿⠟⠛⠛⠿⢿⣿⣿⣿⣿⣿⡿⠋⠉⠉⠉⠙⠻⣿⡇⠀⢸⣿⣿⡏⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠀⠀⠀⢀⡏⠀⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀
⣴⣿⣿⡟⠁⠀⠀⠀⠀⠀⠈⠙⢿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⢸⣿⣿⣧⠀⠀⠀⢠⣾⣿⣿⡿⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠖⠀⣾⠀⠀⢸⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠘⢿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠆⢸⣿⣿⣿⠀⠀⠀⣿⣿⣿⡟⠁⣀⣼⣿⣿⣿⣿⣿⠛⠛⠛⠉⠀⠀⢰⣿⠀⠀⢸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⠿⣿⣦⣤⣀⣀⣤⣤⣾⣿⣿⣦⡀⠀⠀⠀⠀⠀⢀⣀⡤⠂⠘⣿⣿⣿⣷⡀⠸⣿⣿⣿⠁⢠⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣴⠗⠀⣿⣿⡀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⡾⠏⠁⠀⡀⠀⠘⣿⣿⣿⣷⣄⣿⣿⣿⡆⣾⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠁⠀⠀⣿⣿⡇⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⠿⢿⣿⡿⠿⠟⠋⠁⠀⠀⣠⣾⣧⡀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⣿⣿⣿⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣷⡀⠀⠀⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠁⠀⠀⠀⢻⣿⣿⡄⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠶⣶⣾⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣆⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡈⠛⢷⣦⠀⠀⠘⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠁⢀⣰⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠈⠉⠉⠉⠛⠻⠿⢿⣿⣿⣿⣦⠈⢿⣧⠀⠀⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⡇⠸⣿⠀⠀⢿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠚⢿⣿⣿⣿⣟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣧⠀⣿⠀⠀⢸⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣆⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠘⣿⡿⠀⠏⠀⠀⣼⣿⡟⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣧⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⣿⣿⣵⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣦⡀⠸⣿⣿⣧⡀⠀⣀⠀⡀⠙⢿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⢸⡇⠀⠀⠀⣼⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⢻⣿⣿⣷⣾⡏⠀⠙⣶⣤⣿⣿⡇⠘⢿⣿⣿⡆⠀⠀⠀⣸⠀⠀⠀⢰⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⠀⠀⠀⠸⣿⣿⣿⡇⠀⠘⢿⣿⣧⠀⠀⠀⠁⠀⠀⣰⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠃⠀⠀⠀⠀⣿⣿⣿⠃⠀⠀⠸⣿⣿⡄⠀⠀⠀⢀⣴⣿⠛⠁⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡿⠃⠀⠀⠀⠀⢠⣿⣿⡟⠀⠀⠀⠀⢿⣿⡇⠀⠀⠐⠞⠉⠀⣀⣤⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡿⠟⠁⠀⠀⠀⠀⠀⣾⣿⡟⠀⠀⠀⠀⠀⣸⣿⠁⠀⠀⢀⣤⣶⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠞⠛⠁⠀⠀⠀⠀⠀⠀⠀⣼⣿⠏⠀⠀⠀⠀⠀⢠⣿⠇⠀⠀⠀⣸⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⠋⠀⠀⠀⠀⠀⢠⣾⠏⠀⠀⠀⢰⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠟⠋⠀⠀⠀⠀⠀⢀⣴⡿⠃⠀⠀⠀⢠⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⢀⣴⠿⠋⠀⠀⠀⠀⣰⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠋⠁⠀⠀⠀⠀⣠⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠁⠀⠀⠀⠀⠀⣠⣾⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')

    print("Welcome to the Wolf Hunt.")
    print("Your mission is to find the wolf.")

    # Primeira escolha - Encruzilhada
    choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

    if choice1 == "left":
        # Segunda escolha - Floresta
        choice2 = input('You\'ve entered a dense forest. There are paths leading deeper into the woods. Type "walk" to follow the path, or "hide" to look for cover. \n').lower()
        if choice2 == "walk":
            # Terceira escolha - Acampamento
            choice3 = input("You come across an abandoned campsite. There's a tent with a strange smell coming from inside. Do you enter the tent or keep walking? Type 'enter' or 'walk'. \n").lower()
            if choice3 == "enter":
                print("You find the wolf hiding inside the tent! You Win!")
            elif choice3 == "walk":
                print("You continue walking but get lost in the forest. Game Over.")
            else:
                print("That's not a valid option. Game Over.")
        else:
            print("You hide too long and miss your chance to find the wolf. Game Over.")
    else:
        print("You wander off the path and fall into a pit. Game Over.")


# Main code to execute only the project
if __name__ == "__main__":
    # Descomente as atividades para testá-las
    # run_bmi_calculator()  # Descomente para rodar a Atividade 5
    # pizza_order()         # Descomente para rodar a Atividade 6

    # Executando o Projeto Final - Treasure Island
    wolf_hunt()
