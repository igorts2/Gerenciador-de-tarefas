

#verifica se o arquivo já existe!
def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


#cria o arquivo de texto!
def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('falha na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


#leitura do arquivo!
def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print('\033[35mLista de tarefas\033[m')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'''*{dado[0]:<30}
Descrição: {dado[1]:>3}
status: {dado[2]:>3}''')
        
    
#cadastrar nova tarefa no arquivo! 
def cadastrar(arq, tarefa = 'título!', descrição = 'descrição da tarefa', status = 'Não concluido'):
    
     a = open(arq, 'a')
     a.write(f'{tarefa};{descrição};{status}\n')
     a.close()

#Marcar uma tarefa como concluida!
def marcar_como_concluido(arq):
    try:
        with open(arq, 'r') as arquivo:
            linhas = arquivo.readlines()
        
        print('Tarefas disponíveis:')
        tarefas_disponiveis = []
        for i, linha in enumerate(linhas):
            dado = linha.split(';')
            titulo = dado[0]
            status = dado[2].strip()
            tarefas_disponiveis.append((titulo, status))
            print(f'{i + 1}. Tarefa: {titulo}, Status: {status}')
        
        if not tarefas_disponiveis:
            print('Não há tarefas disponíveis.')
            return
        
        escolha = int(input('\033[32mDigite o número da tarefa que deseja marcar como concluída:\033[m '))
        
        if 1 <= escolha <= len(tarefas_disponiveis):
            titulo, status = tarefas_disponiveis[escolha - 1]
            if status == 'Não concluido':
                linhas[escolha - 1] = f'{titulo};{dado[1]};Concluído\n'
                with open(arq, 'w') as arquivo:
                    arquivo.writelines(linhas)
                print(f'A tarefa "{titulo}" foi marcada como concluída.')
            else:
                print(f'A tarefa "{titulo}" já está concluída.')
        else:
            print('Escolha inválida.')

    except Exception as e:
        print(f'Erro ao marcar a tarefa como concluída: {e}')

# Excluir uma tarefa do arquivo
def excluir_tarefa(arq):
    try:
        with open(arq, 'r') as arquivo:
            linhas = arquivo.readlines()
        
        print('Tarefas disponíveis:')
        tarefas_disponiveis = []
        for i, linha in enumerate(linhas):
            dado = linha.split(';')
            titulo = dado[0]
            status = dado[2].strip()
            tarefas_disponiveis.append((titulo, status))
            print(f'{i + 1}. Tarefa: {titulo}, Status: {status}')
        
        if not tarefas_disponiveis:
            print('Não há tarefas disponíveis.')
            return
        
        escolha = int(input('Digite o número da tarefa que deseja excluir: '))
        
        if 1 <= escolha <= len(tarefas_disponiveis):
            titulo, _ = tarefas_disponiveis[escolha - 1]
            del linhas[escolha - 1]
            with open(arq, 'w') as arquivo:
                arquivo.writelines(linhas)
            print(f'A tarefa "{titulo}" foi excluída.')
        else:
            print('Escolha inválida.')

    except Exception as e:
        print(f'Erro ao excluir a tarefa: {e}')


