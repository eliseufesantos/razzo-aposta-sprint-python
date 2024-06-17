# Bibliotecas para gerar aleatoriedade e limpar o terminal
import random
import os

# Cores usadas no terminal
cores = {
    'reset': '\033[0m',
    'preto': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'roxo': '\033[34m',
    'rosa': '\033[35m',
    'ciano': '\033[36m',
    'branco': '\033[37m'
}

saldo = 100.0  # Saldo inicial do usuário
carros = ["vermelho", "azul", "verde"]  # Lista global de carros disponíveis


def limpar_terminal():

    """ Função para limpar o terminal"""

    os.system('cls')

def voltar():

    """ Função para voltar"""

    input(cores['ciano']+"\nPressione ENTER para continuar..."+cores["reset"])

def exibir_saldo(saldo:float):

    """ Função para exibir o saldo atual do usuário. O parâmetro saldo representa a variável global saldo."""

    print(cores["amarelo"]+f"Seu saldo atual é: {saldo:.2f} moedas."+cores["reset"])

def obter_aposta(saldo:float):

    """ Função para obter a aposta do usuário. O parâmetro saldo representa a variável global saldo."""

    while True:
        try:
            aposta = float(input(cores["ciano"]+"Digite o valor da sua aposta: "+cores["reset"]))
            if aposta <= 0:
                print(cores["vermelho"]+"A aposta deve ser um valor positivo."+cores["reset"])
            elif aposta > saldo:
                print(cores["vermelho"]+"Você não tem saldo suficiente para essa aposta."+cores["reset"])
            else:
                return aposta
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def obter_escolha_carro(carros:list):

    """ Função para obter a escolha do carro do usuário. O parâmetro carros representa a lista global carros."""

    while True:
        escolha = input(f"Escolha um carro para apostar ({', '.join(carros)}): ").lower()
        if escolha in carros:
            return escolha
        else:
            print("Escolha inválida. Por favor, escolha entre os carros disponíveis.")

def simular_corrida(carros:list):

    """ Função para simular a corrida e determinar o vencedor. O parâmetro carros representa a lista global carros."""

    vencedor = random.choice(carros)
    return vencedor

def comprar_mais_moedas():

    """ Função para permitir ao usuário comprar mais moedas"""

    print(cores["ciano"]+"\nOpções de compra de moedas:"+cores["reset"])
    print("1. Receber 100 moedas por R$ 10.00")
    print("2. Receber 50 moedas por R$ 5.00")
    print("3. Receber 25 moedas por R$ 2.50")
    
    while True:
        escolha = input(cores["ciano"]+"Escolha uma opção (1, 2 ou 3): "+cores["reset"])
        match escolha:
            case "1":
                return 100, 10.00
            case "2":
                return 50, 5.00
            case "3":
                return 25, 2.50
            case _:
                print(cores["vermelho"]+"Opção inválida. Por favor, escolha 1, 2 ou 3."+cores["reset"])

# Bloco principal
while True:
    limpar_terminal()
    print(cores["verde"]+"Bem-vindo ao RAZZO, jogo de apostas em corrida de Formula E!"+cores["reset"])
    print(cores["ciano"]+"\nMENU PRINCIPAL"+cores["reset"])
    print("1. Apostar")
    print("2. Verificar Saldo")
    print("3. Compre mais moedas")
    print(cores["vermelho"]+"4. Sair"+cores["reset"])
    
    escolha = input(cores["ciano"]+"Escolha uma opção (1, 2, 3 ou 4): "+cores["reset"])
    
    match escolha:
        case "1": # Apostar
            limpar_terminal()
            aposta = obter_aposta(saldo)
            carro_escolhido = obter_escolha_carro(carros)
            vencedor = simular_corrida(carros)
            
            print(f"\nO carro vencedor é: {vencedor}")
            
            if carro_escolhido == vencedor:
                saldo += aposta
                print(cores["verde"]+f"Parabéns! Você ganhou {aposta:.2f} moedas."+cores["reset"])
            else:
                saldo -= aposta
                print(cores["vermelho"]+f"Você perdeu {aposta:.2f} moedas."+cores["reset"])
            
            exibir_saldo(saldo)
            voltar()  
        
        case "2": # Verificar Saldo
            limpar_terminal()
            exibir_saldo(saldo)
            voltar()  
        
        case "3": # Comprar mais moedas
            limpar_terminal()
            qtd_moedas, valor_reais = comprar_mais_moedas()
            saldo += qtd_moedas
            print(cores["verde"]+f"\nVocê comprou {qtd_moedas} moedas por R$ {valor_reais:.2f}."+cores["reset"])
            exibir_saldo(saldo)
            voltar()  
        
        case "4": # Sair
            limpar_terminal()
            print(cores["verde"]+"Obrigado por jogar!"+cores["reset"])
            break
        
        case _:
            print(cores["vermelho"]+"Opção inválida. Por favor, escolha 1, 2, 3 ou 4."+cores["reset"])
            voltar()  
