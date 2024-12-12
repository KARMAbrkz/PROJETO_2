def carregar_arquivo(file1: str):
    archive = open(file1, 'r')
    lines = archive.readlines()
    archive.close()
    return lines


def escrever_arquivo(file1: str, line: int, text):
    try:
        archive = open(file1, 'r')
        lines = archive.readlines()
        archive.close()

        lines[line] = str(text) + '\n'

        archive = open(file1, 'w')
        archive.writelines(lines)
        archive.close()

        carregar_arquivo(file1)
        return lines
    except (IndexError, FileNotFoundError, TypeError, ValueError):
        return 'Parâmetros inválidos'


def cadastrar_evento(eventos, login):
    nmevento = input('nome do evento: ')
    duracao = input('duracao do evento: ')
    local = input('local do evento: ')
    horario = input('horario de inicio: ')
    valor_inscricao = input('valor da inscricao: ')
    descricao = input('descricao do evento: ')
    eventos.append([nmevento, duracao, local, horario, login, valor_inscricao, list, descricao, int(valor_inscricao)])
    print('\nevento cadastrado com sucesso')


def remover_evento(eventos, login):
    nome_evento = input('nome do evento para remover: ')
    i = 0
    while i < len(eventos):
        if eventos[i][0] == nome_evento and eventos[i][4] == login:
            eventos.remove(eventos[i])
            print('evento removido com sucesso')
            break
        i += 1
    else:
        print('evento nao encontrado ou voce nao tem permissao')


def buscar_evento(eventos):
    nome_busca = input('nome do evento para buscar: ')
    i = 0
    while i < len(eventos):
        if eventos[i][0] == nome_busca:
            print(
                f'\nNome: {eventos[i][0]}\nDuracao: {eventos[i][1]}\nLocal: {eventos[i][2]}\nHorario: {eventos[i][3]}\nValor: {eventos[i][5]}\nDescricao: {eventos[i][7]}')
            break
        i += 1
    else:
        print('evento nao encontrado')


def listar_participantes(eventos, login):
    nome_evento = input('nome do evento para ver participantes: ')
    i = 0
    while i < len(eventos):
        if eventos[i][0] == nome_evento and eventos[i][4] == login:
            print('participantes:')
            j = 0
            while j < len(eventos[i][6]):
                print(f'nome: {eventos[i][6][j][0]}, status pagamento: {eventos[i][6][j][1]}')
                j += 1
            break
        i += 1
    else:
        print('evento nao encontrado ou voce nao tem permissao')


def adicionar_participantes(eventos, participante, proibidos):
    nome_evento = input('Digite o nome do evento: ')

    if participante in proibidos:
        print('')
        print('Essa pessoa está proibida dos eventos, motivo:')
        print(proibidos[participante])
        return

    for evento in eventos:
        if evento[0] == nome_evento:
            if participante in evento[6]:
                print(evento[6])
                print('Esse participante já está inscrito no evento.')
            else:
                evento[6].append(participante)
                print(evento[6])
                print(f'Participante {participante} adicionado ao evento {nome_evento}.')
            return
    print('Evento não encontrado.')


def listar_participantes(eventos):
    nome_evento = input('Digite o nome do evento: ')
    lista_de_participantes = []

    for evento in eventos:
        if evento[0] == nome_evento:
            print(f'Evento encontrado: {evento[0]}')
            if evento[6]:
                print('Lista de participantes:')
                for participante in evento[6]:
                    print(f'{participante} salvo')
                    lista_de_participantes.append(participante)
            else:
                print('Nenhum participante encontrado para este evento.')
            escrever_arquivo("lista_de_participantes.txt", 0, str(lista_de_participantes))
            break
    else:
        print('Evento não encontrado.')
    file = carregar_arquivo("lista_de_participantes.txt")
    print(file[0])