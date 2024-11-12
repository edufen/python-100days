# DIA 2

# ATIVIDADE 4 - BMI Calculator
def atividade_4():
    """Calcula o IMC com valores fixos de peso e altura e exibe o resultado"""
    peso = 84
    altura = 1.65
    imc = peso / altura**2
    print("\n--- Calculadora de IMC ---")
    print(f"IMC: {imc:.2f}")


# PROJETO DIA 2 - Tip Calculator
def tip_calculator():
    """Calcula a gorjeta e divide o total da conta entre o número de pessoas"""
    print("\n--- Tip Calculator ---")
    total_bill = float(input("What was the total bill? $"))
    tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))

    # Calcula o valor que cada pessoa deve pagar
    total_per_person = total_bill * (1 + tip_percentage / 100) / people

    # Exibe o valor por pessoa
    print(f"Each person should pay: ${total_per_person:.2f}")


# Main code to execute only the project
if __name__ == "__main__":
    # Descomente as atividades para testá-las
    # atividade_4()   # Descomente para rodar a atividade 4

    # Executando o Projeto Final (Tip Calculator)
    tip_calculator()

