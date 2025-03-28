import json
power = True

def saveContact(contact, file="contatos.json"):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(contact, f, indent=None, ensure_ascii=False)

def loadContacts(file="contatos.json"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

contatos = loadContacts()

def addContact():
    global contatos
    aux_contatos = {}
    joint = str(input("Digite o nome do contato: "))
    aux_contatos["nome"] = joint
    while True:
        try:
            joint = int(input("Digite o número do contato: "))
            break
        except ValueError:
            print("Por favor, digite apenas números (sem hífens e caracteres especiais)")
    aux_contatos["numero"] = joint
    joint = bool(input("O contato é um favorito? (Digite qualquer coisa para marcar contato como favorito):"))
    aux_contatos["favorito"] = joint
    contatos.append(aux_contatos)
    saveContact(contatos)

def listContacts(contacts):
    return sorted(contacts, key=lambda x: x["nome"])
    
def searchContact():
    global contatos
    search = str(input("Digite o nome do contato: "))
    searchAux = []
    for i in contatos:
        if i["nome"] == search:
            searchAux.append(i)
    return sorted(searchAux, key=lambda x: x["nome"])

def editContact():
    whoEdit = 0
    global contatos
    while True:
        try:
            whoEdit = int(input("Digite o índice do contato que deseja editar: "))
            break
        except ValueError:
            print("Por favor, digite apenas números")
    editing = True
    while editing == True:
        print(contatos[whoEdit])
        edit = int(input("O que gostaria de editar?\n1. Nome\n2. Número\n3. Favorito\n4. Parar de editar\nDigite sua escolha:"))
        match edit:
            case 1:
                edit = str(input("Digite o nome novo deste contato: "))
                contatos[whoEdit]["nome"] = edit
            case 2:
                edit = 0
                while True:
                    try:
                        edit = int(input("Digite o novo número deste contato: "))
                        break
                    except ValueError:
                        print("Por favor, digite apenas números (sem hífens e caracteres especiais)")
                contatos[whoEdit]["numero"] = edit
            case 3:
                edit = 0
                while True:
                    try:
                        edit = int(input("Gostaria de mudar o status de favorito deste contato?\n1. Sim\n2. Não\nDigite sua escolha: "))
                        break
                    except ValueError:
                        edit = 2
                if edit == 1:
                    if contatos[whoEdit]["favorito"] == True:
                        contatos[whoEdit]["favorito"] = False
                    else:
                        contatos[whoEdit]["favorito"] = True
            case _:
                saveContact(contatos)
                editing = False
                
def removeContact():
    global contatos
    print(contatos)
    while True:
        try:
            whoDelete = int(input("Digite o índice do contato que gostaria de remover: "))
            break
        except ValueError:
            print("Por favor, digite apenas números")
    contatos.pop(whoDelete)
    saveContact(contatos)
    
def editFavorite():
    global contatos
    print(contatos)
    while True:
        try:
            whoFavorite = int(input("Digite o índice do contato que gostaria de marcar/desmarcar como favorito: "))
            break
        except ValueError:
            print("Por favor, digite apenas números")
    if contatos[whoFavorite]["favorito"] == True:
        contatos[whoFavorite]["favorito"] = False
    else:
        contatos[whoFavorite]["favorito"] = True
    saveContact(contatos)
        
def listFavorites():
    global contatos
    searchAux = []
    for i in contatos:
        if i["favorito"] == True:
            searchAux.append(i)
    return sorted(searchAux, key=lambda x: x["nome"])

while power == True:
    try:
        choose = int(input("1. Adicionar um contato\n2. Listar todos os contatos\n3. Buscar um contato\n4. Atualizar um contato\n5. Remover um contato\n6. Marcar/Desmarcar um contato como favorito\n7. Listar apenas os contatos favoritos\n8. Sair do programa\nDigite sua escolha: "))
    except ValueError:
        choose = 8
    match choose:
        case 1:
            addContact()
        case 2:
            print(listContacts(contatos))
        case 3:
            print(searchContact())
        case 4:
            editContact()
        case 5:
            removeContact()
        case 6:
            editFavorite()
        case 7:
            print(listFavorites())
        case _:
            power = False