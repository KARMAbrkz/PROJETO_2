from funcoes import *
clt = [['fabioallangomes@gmail.com', '1234']]
eventos = [
    ['Corujão dos games', '7h', 'rua domingos lopes, numero 3', '20h', 'fabioallangomes@gmail.com', '20 reais', [], ['madrugada jogando jogos, pagando a inscriçao lanches são de graça'], 20],
    ['show felipe amorim', '3h', 'praca municipal de sousa', '21h', 'admmaster', '50 reais', [], ['show do grande cantor felipe amorim, musicas contagiantes e repertorio novo!'], 50]
]
login = 'nada'
usuarios_proibidos = {'dudu malvado':'muito malvado', 'ig': 'lady gaga'}

while True:
    print('-------plataforma de gerenciamento virtual de eventos--------')
    print('\nmenu principal')
    print('1=quer gereciar ou cadastrar seus eventos? logue por aqui!')
    print('2=quer participar de um evento? logue agora!')
    print('3=nao contem uma conta ainda, cadastre-se!')
    print('4=sair')
    opcao = input('digite uma opcao: ')

    if opcao == '1':
        usr = input('digite seu email: ')
        senha = input('digite sua senha: ')
        if [usr, senha] in clt:
            login = usr
            print('\nlogin realizado com sucesso\n')

            while True:
                print(
                    '\n1=cadastrar evento\n2=remover evento\n3=buscar evento\n4=atualizar evento\n5=listar participantes\n6=ver valor arrecadado\n7=voltar')
                adminfunc = input('escolha uma opcao: ')

                if adminfunc == '1':
                    cadastrar_evento(eventos, login)

                elif adminfunc == '2':
                    remover_evento(eventos, login)

                elif adminfunc == '3':
                    buscar_evento(eventos)

                elif adminfunc == '4':
                    nome_evento = input('nome do evento para atualizar: ')
                    for evento in eventos:
                        if evento[0] == nome_evento and evento[4] == login:
                            evento[0] = input('novo nome do evento: ')
                            evento[1] = input('nova duracao: ')
                            evento[2] = input('novo local: ')
                            evento[3] = input('novo horario: ')
                            evento[5] = input('novo valor da inscricao: ')
                            evento[7] = int(evento[5])
                            evento[6] = input('nova descricao: ')
                            print('evento atualizado com sucesso')
                            break
                    else:
                        print('evento nao encontrado ou voce nao tem permissao')
                elif adminfunc == '5':
                    listar_participantes(eventos)
                elif adminfunc == '6':
                    nome_evento = input('nome do evento para ver valor arrecadado: ')
                    for evento in eventos:
                        if evento[0] == nome_evento and evento[4] == login:
                            total_arrecadado = len(evento[6]) * evento[8]
                            print(
                                f'valor arrecadado: {total_arrecadado} reais\nnumero de inscritos: {len(evento[6])}\nvalor por participante: {evento[5]}')
                            break
                    else:
                        print('evento nao encontrado ou voce nao tem permissao')
                elif adminfunc == '7':
                    break
                else:
                    print('opcao invalida')
        else:
            print('usuario ou senha incorretos')
    elif opcao == '2':
        usr = input('digite seu email: ')
        senha = input('digite sua senha: ')
        if [usr, senha] in clt:
            login = usr
            print('\nlogin realizado com sucesso\n')

            while True:
                print('\n1=ver lista de eventos\n2=inscrever-se em evento\n3=cancelar inscricao\n4=voltar')

                opcao_cliente = input('escolha uma opcao: ')
                if opcao_cliente == '1':
                    for evento in eventos:
                        print(f'evento: {evento[0]}, valor: {evento[5]}, descricao: {evento[7]}')

                elif opcao_cliente == '2':

                    adicionar_participantes(eventos, login, usuarios_proibidos)
                elif opcao_cliente == '3':
                    cancelar_evento = input('evento para cancelar inscricao: ')
                    i = 0
                    while i < len(eventos):
                        if eventos[i][0] == cancelar_evento:
                            j = 0
                            while j < len(eventos[i][6]):
                                if eventos[i][6][j][0] == login:
                                    eventos[i][6].remove(eventos[i][6][j])
                                    print('inscricao cancelada com sucesso')
                                    break
                                j += 1
                            else:
                                print('voce nao esta inscrito nesse evento')
                            break
                        i += 1
                    else:
                        print('evento nao encontrado')
                elif opcao_cliente == '4':
                    break
                else:
                    print('opcao invalida')
        else:
            print('usuario ou senha incorretos')
    elif opcao == '3':
        email = input('digite seu email: ')
        senha = input('digite sua senha: ')
        clt.append([email, senha])
        print('conta criada com sucesso!')

    elif opcao == '4':
        print('\nencerrando...\nprograma encerrado com sucesso')
        break

    else:
        print('\nopcao invalida\n')