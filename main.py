import sys

sys.path.append('classes')
sys.path.append('functions')

from ControladorTelefone import ControladorTelefone
from linha import linha

# carrega os dados iniciais
ControladorTelefone.start()

# novoTelefone = ControladorTelefone.criar({'tipo': 'Celular', 'marca': 'Merdinha', 'modelo': 'Merda', 'valor': 1000})
# ControladorTelefone.salvar(novoTelefone)

while (True):

    try:
        linha(50)
        print("Observações: Informando que o programa faz\ndiferença entre letras maiúsculas e minúculas. \nPara operar, siga as instruções...")
        linha(50)
        print('Escolha uma das opções abaixo:')
        print('[0] Cadastrar')
        print('[1] Listar')
        print('[2] Pesquisar')
        print('[3] Sair')

        ent = int(input())
    except:
        ControladorTelefone.mostrarErro(1)
        continue
        
    if (ent == 0):
        obj = ControladorTelefone.cadastrar()
        if (obj == None):
            continue
        else:
            ControladorTelefone.telefones.append(obj)

    elif (ent == 1):
        if ( (len(ControladorTelefone.telefones)) > 0 ):
            ControladorTelefone.listar()
        else:
            ControladorTelefone.mostrarErro(2)
            continue

    elif (ent == 2):
        if ( (len(ControladorTelefone.telefones)) > 0 ):
            ControladorTelefone.pesquisar(ControladorTelefone.telefones)
        else:
            ControladorTelefone.mostrarErro(2)
            continue

    elif (ent == 3):
            print('Volte mais tarde!')
            break
    else:
        ControladorTelefone.mostrarErro(3)
        continue