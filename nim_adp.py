def computador_comeca(n, m):
    return n % (m + 1) != 0


def computador_escolhe_jogada(n, m):
    if n % (m + 1) == 0:
        return m
    else:
        return n % (m + 1)


def usuario_escolhe_jogada(n, m):
    jogada = 0
    while jogada <= 0 or jogada > m or jogada > n:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada <= 0 or jogada > m or jogada > n:
            print("Oops! Jogada inválida! Tente de novo.")
    return jogada


def partida():
    n = int(input("Quantas peças no tabuleiro? "))
    m = int(input("Limite de peças a serem retiradas por jogada? "))

    if computador_comeca(n, m):
        print("Computador começa!\n")
        jogador_atual = "computador"
    else:
        print("Você começa!\n")
        jogador_atual = "usuario"

    while n > 0:
        if jogador_atual == "usuario":
            jogada = usuario_escolhe_jogada(n, m)
            print("\nVocê tirou", jogada, "peça(s).")
        else:
            jogada = computador_escolhe_jogada(n, m)
            print("\nO computador tirou", jogada, "peça(s).")

        n -= jogada
        print("Agora resta(m)", n, "peça(s) no tabuleiro.\n")

        if n == 0:
            if jogador_atual == "usuario":
                print("Fim do jogo! Você ganhou!\n")
                return "usuario"
            else:
                print("Fim do jogo! O computador ganhou!\n")
                return "computador"
        else:
            jogador_atual = "usuario" if jogador_atual == "computador" else "computador"


def campeonato():
    placar_usuario = 0
    placar_computador = 0

    for rodada in range(1, 4):
        print("\n**** Rodada", rodada, "****\n")
        resultado_partida = partida()
        if resultado_partida == "usuario":
            placar_usuario += 1
        else:
            placar_computador += 1

    print("\n**** Final do campeonato! ****\n")
    print("Placar: Você", placar_usuario, "X", placar_computador, "Computador")

    if placar_usuario > placar_computador:
        print("Você venceu o campeonato!")
    elif placar_computador > placar_usuario:
        print("O computador venceu o campeonato!")
    else:
        print("O campeonato terminou em empate!")


def main():
    print("Bem-vindo ao jogo do NIM!")
    print("Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    opcao = int(input())
    if opcao == 1:
        print("\n**** Partida Única ****\n")
        partida()
    elif opcao == 2:
        print("\n**** Campeonato ****\n")
        campeonato()
    else:
        print("Opção inválida. Encerrando o programa.")


if __name__ == "__main__":
    main()
