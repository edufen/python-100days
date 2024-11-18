# DIA 6

# PROJETO DIA 6 - Reeborg's World Maze (https://reeborg.ca/reeborg.html)
def reeborg_maze():
    """
    Resolve o labirinto no Reeborg's World utilizando uma abordagem
    baseada em sempre seguir pela direita.
    """

    def turn_right():
        turn_left()
        turn_left()
        turn_left()

    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()


# Main code para executar apenas o projeto
if __name__ == "__main__":
    # Não há atividades neste dia, apenas o projeto.

    # Executando o Projeto Final (Reeborg's World Maze)
    reeborg_maze()
