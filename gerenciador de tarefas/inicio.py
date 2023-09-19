from app import menu
from app import erro
from app.arquivo import *

# Arquivo que será criado!
arq = 'lista_de_tarefas.txt'

if not arquivoexiste(arq):
    criararquivo(arq)


while True:
    menu.msgmenu()
    valor = erro.pergunta()

    
    if valor == 1:
        menu.resposta1()
        lerarquivo(arq)
        # Opção de listar o conteudo de um arquivo!
    if valor == 2:
        menu.resposta2()
        tarefa = str(input('Título da tarefa: '))
        descrição = str(input('descrição da tarefa: '))
        cadastrar(arq, tarefa, descrição)
        # Opção para cadastrar uma nova tarefa!
    if valor == 3:
        menu.resposta3
        marcar_como_concluido(arq)
        # Opção para marcar uma tarefa como concluida!
    if valor == 4:
        menu.resposta4()
        excluir_tarefa(arq)
        # Opção para excluir uma tarefa!
    if valor == 5:
        menu.resposta5()
        print('Fim do sistema!')
        raise SystemExit()
        #Opção para sair do sistema!
    