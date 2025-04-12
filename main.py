import json

def inputCliente():
    nome = input('Qual seu nome: ')
    cpf = input('Qual seu cpf: ')
    qtdPessoa = input('Qual a quantidade de pessoas: ')
    qtdCamas = input('Qual a quantidadede camas: ')

    cadastro = {
        'nome':nome,
        'cpf':cpf,
        'qtdPessoa':qtdPessoa,
        'qtdCamas':qtdCamas
    }
    
    return cadastro


def reserva_quarto():
    hotel = ler_json_hotel('hotel.json')

    if hotel['quartosOcupados'] != 0:
        hotel['quartosOcupados'] -= 1
        with open('hotel.json','w',encoding='utf8') as h:
            json.dump(hotel,h,ensure_ascii=False,indent=4)

        print("A reserva foi feita com secesso")

        return
    print("Não temos reserva")


def mostrar_disponibilidade_quartos():
    hotel = ler_json_hotel('hotel.json')
    print(f'Quartos livres: {hotel['quartosTotais'] - hotel['quartosOcupados']}')

def ler_json_hotel(db):
    with open(db,'r') as h:
        hotel = json.load(h)
    return hotel

def salvando_cliente(cadastro):
    if type(cadastro) != 'dict':
        with open('clientes.json','r') as c:
            clientes = json.load(c)

        clientes.append(cadastro)
        with open('clientes.json','w',encoding='utf8') as c:
            json.dump(clientes,c,ensure_ascii=False,indent=4)

cliente1 = inputCliente()
salvando_cliente(cliente1)
reserva_quarto()
mostrar_disponibilidade_quartos()

