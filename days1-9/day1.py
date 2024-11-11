# DIA 1

# ATIVIDADE 1 - Printar uma receita completa
def atividade_1():
    """Imprime uma receita completa como uma lista de etapas"""
    receita = [
        "1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.",
        "2. Knead the dough for 10 minutes.",
        "3. Add 3g of Salt.",
        "4. Leave to rise for 2 hours.",
        "5. Bake at 200 degrees C for 30 minutes."
    ]
    print("\n--- Receita Completa ---")
    for item in receita:
        print(item)


# ATIVIDADE 2 - Consertar o código (Exemplo simples)
def atividade_2():
    """Explica como usar print e concatenação de strings"""
    print("\n--- Notes from Day 1 ---")
    print("The print statement is used to output strings")
    print("Strings are strings of characters")
    print("String Concatenation is done with the + sign")
    print("New lines can be created with a \\ and the letter n")


# ATIVIDADE 3 - Inverter os valores das variáveis
def atividade_3():
    """Inverte os valores das variáveis 'glass1' e 'glass2' sem usar as palavras 'milk' e 'juice'"""
    glass1 = "milk"
    glass2 = "juice"
    glass1, glass2 = glass2, glass1
    print("\n--- Inverter os valores ---")
    print(f"glass1: {glass1}, glass2: {glass2}")


# PROJETO DIA 1 - "Band Name Generator Project"
def band_name_generator():
    """Gera um nome de banda baseado na cidade e no nome do pet"""
    print("\n--- Band Name Generator ---")
    city = input("What's the name of the city you grew up in?\n")
    pet = input("What's your pet's name?\n")
    print(f"Your band name could be {city} {pet}")


# Main code to execute only the project
if __name__ == "__main__":
    # Descomente as atividades para testá-las
    # atividade_1()   # Descomente para rodar a atividade 1
    # atividade_2()   # Descomente para rodar a atividade 2
    # atividade_3()   # Descomente para rodar a atividade 3

    # Executando o Projeto Final (Band Name Generator)
    band_name_generator()
