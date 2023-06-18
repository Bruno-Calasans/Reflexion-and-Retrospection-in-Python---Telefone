import json
from Celular import Celular
from Smartphone import Smartfone
from TelefoneMovel import TelefoneMovel
from linha import linha


ErrorsDict = dict({
    1: "ERRO. Você deve ter digitado algo errado.",
    2: "Desculpe, mas não há ítens. Cadastre algum item primeiro.",
    3: "OPÇÃO INVÁLIDA"
})

class ControladorTelefone:

    telefones: list[TelefoneMovel] = []

    def start():
        telefoneLista = ControladorTelefone.lerTelefones()
        ControladorTelefone.limparTelefones()
        ControladorTelefone.mudarTelefones(telefoneLista)

    def lerTelefones() -> list[TelefoneMovel] :

        file = open('./data/default.json', 'r')
        text = file.read()
        file.close()

        telefoneLista = json.loads(text)
        telefoneListClass = []

        for telefone in telefoneLista:
            telefoneListClass.append(ControladorTelefone.criar(telefone))

        return telefoneListClass

    def criarDicionarioTelefone(telefone: TelefoneMovel):

        return {
            'tipo': telefone.tipo,
            'marca': telefone.marca,
            'modelo': telefone.modelo,
            'valor': telefone.valor
        }

    def pegarTelefones():
        return ControladorTelefone.telefones

    def mudarTelefones(telefones: list[TelefoneMovel]):
        ControladorTelefone.telefones = telefones

    def limparTelefones():
        ControladorTelefone.telefones.clear()

    def salvar(telefone: TelefoneMovel):
         telefoneLista = ControladorTelefone.lerTelefones()
         telefoneLista.append(telefone)

         teleSerializado = []

         for tel in telefoneLista:
            teleSerializado.append(tel.__dict__)
        
         telefoneListaTexto = json.dumps(teleSerializado)

         file = open('./data/default.json', 'w')
         file.write(telefoneListaTexto)
         file.close()

    def criar(obj: object):
        tipo = obj['tipo']
        marca = obj['marca']
        modelo = obj['modelo']
        valor = obj['valor']

        novoTelefone = None

        if tipo == 'Celular':
            novoTelefone = Celular(marca, modelo, valor)
        else:
           novoTelefone = Smartfone(marca, modelo, valor)

        return novoTelefone

    def inserir(telefone: TelefoneMovel):
        ControladorTelefone.telefones.append(telefone)

    def cadastrar():
        r = None
        
        try:
            linha(50)
            print('Cadastrar Telefone'.upper().center(50))
            linha(50)
            tip = input("\nDigite 'Celular' ou 'Smartfone': ").capitalize()
            mar = input("Marca: ")
            mod = input("Modelo: ")
            val = float(input("Valor: R$ "))
            
            r = eval( "%s(mar, mod, val)" %(tip) )

            novoTelefone = ControladorTelefone.criar({'tipo': tip, 'marca': mar, 'modelo': mod, 'valor': val})
            ControladorTelefone.inserir(novoTelefone)
            ControladorTelefone.salvar(novoTelefone)
            
        except:
            ControladorTelefone.mostrarErro(1)
        else:
            print("Obrigado, o %s %s %s custando RS %.2f, foi cadastrado."
                %(tip, mar, mod, val))
        finally:
            return r

    def listar():
        for i in  ControladorTelefone.telefones:
            i.impInfos()

    def pesquisar(tlFones:list):
    
        l: list[TelefoneMovel] = []
        # Para saídas 'completas' (com características)
        s = "Pesquisando para você:\n"
        # Para saídas 'incompletas' (sem características)
        s1 = ""
        classes = [Celular, Smartfone]
        # Apenas para ajudar a testar a validade da informação digitada
        caractBase = ["marca", "modelo"]
        caract = []
        # Apenas informação
        infor = ""
        # Valores do que se procura
        valores = []
        # Comparadores (== ou !=
        comps = []
        
        try:
            linha(50)
            print('Pesquisar Telefone'.upper().center(50))
            linha(50)
            print('[0] Pesquisar por Celular')
            print('[1] Pesquisar por Smartfone')
            print('[2] Pesquisar por Ambos')
            ent = int(input('Digite a opção desejada: '))
            
            if (ent == 2):
                l = tlFones[:]
                s = s + "Celular ou Smartfone\n"
            elif (ent > -1):
                s = s + classes[ent].__name__ + "\n"
                for i in tlFones:
                    if ( (type(i)) is (classes[ent]) ):
                        l.append(i)
            else:
                ControladorTelefone.mostrarErro(1)
                return
            s1 = s[:]
        except:
            ControladorTelefone.mostrarErro(1)
            return

        try:
            ent = input("\nDeseja selecionar alguma característica de marca e/ou modelo? Se sim, digite a característica e depois '_,_'. Se não, apenas digite algo:\n").strip().split("_,_")
            if ( (len(ent)) > 0 ):
                for i in caractBase:
                    for j, k in enumerate(ent):
                        if (i == k):
                            m = ent.pop(j)
                            caract.append( m )
                            infor = infor + ", " + m
            if ( (len(caract)) > 0):
                print("\nSelecionado, por você%s." %infor)
            else:
                print("\nVocê não selecionou alguma característica.")
        except:
            ControladorTelefone.mostrarErro(1)
            return

        if ( (len(caract)) > 0 ):
            segue = False

            try:
                for i in caract:
                    ent = input("\nDigite um valor para %s seguido de '.' para um valor igual ou '!' para um valor diferente\n" %i).strip()
                    if (ent[-1] == "."):
                        valores.append( ent[:-1] )
                        s = s + i + " igual a " + ent[:-1] + " "
                        comps.append("==")

                    elif (ent[-1] == "!"):
                        valores.append( ent[:-1] )
                        s = s + i + " diferente de " + ent[:-1] + " "
                        comps.append("!=")
                        
                    else:
                        ControladorTelefone.mostrarErro(1)
                        break
                else:
                    segue = True
                if (segue == False):
                    return
            except:
                ControladorTelefone.mostrarErro(1)
                return

            try:
                print("\n%s" %s)
                for i in l:
                    tel = vars(i)
                    texsDaPesq = []
                    texDaPesqTot = ""

                    for j, k in enumerate(caract):
                        texsDaPesq.append( "(tel.get('" + k + "')" + comps[j] + "'" + valores[j] + "')" + " and ")

                    texsDaPesq[-1] = texsDaPesq[-1][:-5]
                    for j in texsDaPesq:
                        texDaPesqTot = texDaPesqTot + j
                    
                    texDaPesqTot = "True if( " + texDaPesqTot + " ) else False"
                    if ( (eval("%s"%texDaPesqTot)) == True ):
                        i.impInfos()

            except:
                ControladorTelefone.mostrarErro(3)
                return

        else:
            print(s1)
            for i in l:
                i.impInfos()

    def mostrarErro(cod: int):
        print(ErrorsDict[cod])

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)