import numpy as np

tabela = {
    **{chr(i): i - 64 for i in range(65, 91)},
    **{chr(i).lower(): i - 64 for i in range(65, 91)},
    **{chr(i): 53 + i for i in range(10)}
}
# Função para codificar a mensagem em uma matriz
def codificar_mensagem(mensagem):
    if len(mensagem) != 6:
        raise ValueError("A mensagem deve ter 6 caracteres")
    
    M = np.zeros((3, 2), dtype=int)
    for i in range(3):
        for j in range(2):
            M[i, j] = tabela.get(mensagem[j * 3 + i])
    return M

# Função para criptografar a mensagem
def criptografar_mensagem(mensagem, C):
    M = codificar_mensagem(mensagem)
    MC = np.dot(C, M)
    return M, MC

# Função para descriptografar a mensagem criptografada
def descriptografar_mensagem(MC, C):
    C_inv = np.linalg.inv(C)
    M = np.dot(C_inv, MC).astype(int)
    return M

# Função para decodificar a matriz em uma mensagem
def decodificar_mensagem(M):
    inv_tabela = {v: k for k, v in tabela.items()}
    mensagem = ''
    for j in range(2):
        for i in range(3):
            mensagem += inv_tabela[M[i, j]]
    return mensagem

# Função principal
def main():
    mensagem = input("Digite uma mensagem de 6 caracteres: ")

# Matriz de criptografia (3x3)
    C = np.array([
    [1, 0, 1],
    [1, 1, 1],
    [0, 2, -1]
])

# Criptografar a mensagem
    M, MC = criptografar_mensagem(mensagem, C)

    print("Mensagem original: ", mensagem)
    print("Matriz M codificada: ")
    print(M)
    print("Matriz da mensagem criptografada MC: ")
    print(MC)

# Descriptografar a mensagem
    MC_input = input("Digite a matriz de mensagem criptografada (6 valores, separados por espaço): ")
    MC_input = list(map(int, MC_input.split()))
    MC = np.array(MC_input).reshape((3, 2))

    M_descriptografada = descriptografar_mensagem(MC, C)
    mensagem_original = decodificar_mensagem(M_descriptografada)

    print("Matriz MC lida: ")
    print(MC)
    print("Matriz M descriptografia: ")
    print(M_descriptografada)
    print("Mensagem original enviada: ", mensagem_original)

if __name__ == "__main__":
    main()