import operacoes
import this
this.opcao = -1

def menu():
    print('\n\nEscolha uma das opções abaixo: \n\n' +
            '1. Cadastrar\n'                        +
            '2. Consultar\n'                        +
            '3. Atualizar nome\n'                   +
            '4. Atualizar telefone\n'               +
            '5. Atualizar endereço\n'               +
            '6. Atualizar data atual\n'             +
            '7. Excluir\n'                          +
            '0. Sair')
    this.opcao = int(input())

def operacao():
    while(this.opcao != 0):
        menu()
        if this.opcao == 1:
            # Coletando a digitação do usuário
            print('Digite o nome: ')
            nome = input()
            print('Digite o telefone: ')
            telefone = input()
            print('Digite o endereço: ')
            endereco = input()
            print('Digite a data atual: ')
            data = input()
            # utilizar o método cadastrar
            operacoes.inserir(nome, telefone, endereco, data)
        elif this.opcao == 2:
            operacoes.selecionar()
        elif this.opcao == 3:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigo = input()
            print('Informe o novo nome: ')
            nome = input()
            # Uso do método
            operacoes.atualizarNome(codigo, nome)
        elif this.opcao == 4:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigo = input()
            print('Informe o novo telefone: ')
            telefone = input()
            # Uso do método
            operacoes.atualizarTelefone(codigo, telefone)
        elif this.opcao == 5:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigo = input()
            print('Informe o novo endereço: ')
            endereco = input()
            # Uso do método
            operacoes.atualizarEndereco(codigo, endereco)
        elif this.opcao == 6:
            # Coletando a digitação do usuário
            print('Informe o código: ')
            codigo = input()
            print('Informe o novo data atual: ')
            data = input()
            # Uso do método
            operacoes.atualizarData(codigo, data)
        elif this.opcao == 7:
            print('Informe o código: ')
            codigo = input()
            operacoes.excluir(codigo)
        elif this.opcao == 0:
            print('Obrigado!')
