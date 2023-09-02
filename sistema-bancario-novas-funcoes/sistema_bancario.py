
def depositar(saldo, valor, extrato, /):
        if valor > 0:
                saldo += valor
                extrato += f'DEPÓSITO:  R$ {valor:.2f}\n'
                numero_saques += 1
                
        else:
                print("Valor inválido!")
        return


def main():
        menu = '''Qual operação você deseja realizar:
                     [1] - Deposito
                     [2] - Saque
                     [3] - Extrato
                     [4] - Sair
Digite o numero da opcao desejada: '''

        nome_usuario = input("Olá qual é o seu nome? ")
        print(f'Seja bem vindo(a) {nome_usuario} ao nosso banco!')
        #o sistema de fazer: saque, deposito e extrato

        extrato = ""
        saldo = float(0)
        SAQUE_LIMITE = 3
        AGENCIA = '0001'
        limite = 500
        numeros_saques = 0

        while True:
                operacao = int(input(menu))

                if operacao == 1:
                        valor = float(input('Qual o valor do depósito?'))
                        saldo, extrato = depositar(saldo, valor, extrato)
                        
        
                elif operacao == 2:
                        valor = float(input("Valor do saque:"))

                        saldo, extrato = sacar(
                                saldo = saldo,
                                valor=valor,
                                extrato=extrato,
                                limite=limite,
                                numero_saques=numero_saques
                        )
                        excedeu_saldo = saque_valor > valor
                        excedeu_limite = valor > limite
                        excedeu_saques = numeros_saques >= SAQUE_LIMITE

                        if excedeu_saldo:
                                print("saldo insuficiente")
                        elif excedeu_limite:
                                print("excedeu limite")
                        elif excedeu_saques:
                                print("excedeu limites de saques")

                        elif valor > 0:
                                saldo -= valor
                                extrato += f'DEPÓSITO:  R$ {valor:.2f}\n'
                                numeros_saques += 1

                        else:
                                print("valor inválido")
        
        
                
                elif operacao == 3:
                        print(f'\nSaldo: R$ {saldo:.2f}')

                elif operacao == 4:
                        break
                
                else:
                        print("Essa opção não é válida")