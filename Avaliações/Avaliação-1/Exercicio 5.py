import random

def obter_escolha_computador():
    return random.choice(['pedra', 'papel', 'tesoura']) #computador vai pegar um valor aleatorio


def determinar_vencedor(escolha_usuario, escolha_computador):
    if escolha_usuario == escolha_computador:
        return 'empate'
    elif (
            (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or
            (escolha_usuario == 'papel' and escolha_computador == 'pedra') or
            (escolha_usuario == 'tesoura' and escolha_computador == 'papel')
    ):
        return 'usuario'
    else:
        return 'computador'

vitorias_usuario = 0
vitorias_computador = 0
empates = 0

while True:
    escolha_usuario = input("Escolha pedra, papel ou tesoura (ou 'parar' para encerrar): ").lower()

    if escolha_usuario == 'parar':
        break

    if escolha_usuario not in ['pedra', 'papel', 'tesoura']:
        print("Escolha inválida. Tente novamente.")
        continue

    escolha_computador = obter_escolha_computador()
    print(f"Computador escolheu: {escolha_computador}")

    resultado = determinar_vencedor(escolha_usuario, escolha_computador)
    if resultado == 'usuario':
        print("Você venceu!")
        vitorias_usuario += 1
    elif resultado == 'computador':
        print("Computador venceu!")
        vitorias_computador += 1
    else:
        print("Empate!")
        empates += 1

print("\nResultados finais:")
print(f"Vitórias do usuário: {vitorias_usuario}")
print(f"Vitórias do computador: {vitorias_computador}")
print(f"Empates: {empates}")
