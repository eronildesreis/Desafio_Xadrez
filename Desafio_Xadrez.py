# Classe para representar o tabuleiro de xadrez
class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],  # Primeira linha (peças brancas)
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],  # Segunda linha (peões brancos)
            ['.', '.', '.', '.', '.', '.', '.', '.'],  # Terceira linha (vazia)
            ['.', '.', '.', '.', '.', '.', '.', '.'],  # Quarta linha (vazia)
            ['.', '.', '.', '.', '.', '.', '.', '.'],  # Quinta linha (vazia)
            ['.', '.', '.', '.', '.', '.', '.', '.'],  # Sexta linha (vazia)
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],  # Sétima linha (peões pretos)
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']   # Oitava linha (peças pretas)
        ]

    # Função para imprimir o tabuleiro
    def imprimir(self):
        for linha in self.tabuleiro:
            print(" ".join(linha))
        print("\n")

    # Função para mover uma peça
    def mover(self, origem, destino):
        linha_origem, coluna_origem = origem
        linha_destino, coluna_destino = destino

        # Validando a posição de origem e destino
        if self.tabuleiro[linha_origem][coluna_origem] == '.':
            print("Não há peça na posição de origem!")
            return False
        if linha_destino < 0 or linha_destino > 7 or coluna_destino < 0 or coluna_destino > 7:
            print("Destino fora do tabuleiro!")
            return False

        # Movimento simples: substitui a posição de destino pela peça da origem
        self.tabuleiro[linha_destino][coluna_destino] = self.tabuleiro[linha_origem][coluna_origem]
        self.tabuleiro[linha_origem][coluna_origem] = '.'  # Limpa a posição de origem

        return True

# Função para converter as posições de xadrez (ex: 'a2', 'e4')
def converter_posicao(posicao):
    coluna = ord(posicao[0].lower()) - ord('a')
    linha = 8 - int(posicao[1])
    return (linha, coluna)

# Função principal para o jogo
def jogar_xadrez():
    tabuleiro = Tabuleiro()
    tabuleiro.imprimir()

    while True:
        # Solicitar ao jogador a posição de origem e destino
        origem = input("Digite a posição de origem (ex: a2): ")
        destino = input("Digite a posição de destino (ex: a4): ")

        # Converter as posições para índices de lista
        origem = converter_posicao(origem)
        destino = converter_posicao(destino)

        # Tentar mover a peça
        if tabuleiro.mover(origem, destino):
            tabuleiro.imprimir()
        else:
            print("Movimento inválido, tente novamente!")

if __name__ == "__main__":
    jogar_xadrez()