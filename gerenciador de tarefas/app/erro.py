

def pergunta():
    while True:
        try:
            op = int(input('Qual a sua opção: '))
            if op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
                print(f'ERRO!!! Selecione apenas uma das opções (1, 2, 3, 4 ou 5)!')
            else:
                return op
        except ValueError:
            print(f'ERRO!!! Selecione apenas uma das opções (1, 2, 3, 4 ou 5)!')
        
