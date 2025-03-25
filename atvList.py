power = True
contatos = []
while power == True:
    choose = int(input("1. Adicionar um contato\n2. Listar todos os contatos\n3. Buscar um contato\n4. Atualizar um contato\n5. Remover um contato\n6. Marcar/Desmarcar um contato como favorito\n7. Listar apenas os contatos favoritos\n8. Sair do programa\nDigite sua escolha: "))
    match choose:
        case 1:
            aux_contatos = {}
            joint = str(input("Digite o nome do contato: "))
            aux_contatos["nome"] = joint
            joint = str(input("Digite o número do contato: "))
            aux_contatos["numero"] = joint
            joint = bool(input("O contato é um favorito? (Digite True ou False):"))
            aux_contatos["favorito"] = joint
            contatos.append(aux_contatos)
            aux_contatos = {}
        case 2:
            contatosShow = contatos.sort()
            print(contatosShow)
            contatosShow = []
        case 3:
            search = str(input("Digite o nome do contato: "))
            searchAux = []
            for i in contatos:
                if i["nome"] == search:
                    searchAux.append(i)
            print(searchAux.sort())
            searchAux = []
        case 4:
            whoEdit = int(input("Digite o índice do contato que deseja editar: "))
            editing = True
            while editing == True:
                print(contatos[whoEdit])
                edit = str(input("O que gostaria de editar?\n1. Nome\n2. Número\n3. Favorito\n4. Parar de editar\nDigite sua escolha:"))
                match choose:
                    case 1:
                        edit = str(input("Digite o nome novo deste contato: "))
                        whoEdit["nome"] = edit
                    case 2:
                        edit = str(input("Digite o novo número deste contato: "))
                        whoEdit["numero"] = edit
                    case 3:
                        edit = bool(input("Gostaria de mudar o status de favorito deste contato?\n1. Sim\n2. Não\nDigite sua escolha: "))
                        if edit == 1:
                            if whoEdit["favorito"] == True:
                                whoEdit["favorito"] = False
                            else:
                                whoEdit["favorito"] = True
                    case 4:
                        editing = False
        case 5:
            print(contatos)
            whoDelete = int(input("Digite o índice do contato que gostaria de remover: "))
            contatos.pop(whoDelete)
        case 6:
            print(contatos)
            whoFavorite = int(input("Digite o índice do contato que gostaria de marcar/desmarcar como favorito: "))
            if contatos[whoFavorite["favorito"]] == True:
                contatos[whoFavorite["favorito"]] = False
            else:
                contatos[whoFavorite["favorito"]] = True
        case 7:
            searchAux = []
            for i in contatos:
                if i["favorito"] == True:
                    searchAux.append(i)
            print(searchAux.sort())
            searchAux = []
        case 8:
            power = False