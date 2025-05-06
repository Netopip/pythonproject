from datetime import datetime

def verificar_data(data_str):
    """
    A função verificar_data tenta converter a string data_str para um objeto datetime usando o formato especificado ('%d/%m/%Y'). Se a conversão for bem-sucedida, a data é válida e a função retorna True. Se ocorrer um ValueError, a data é inválida e a função retorna False.

    """
    try:
        # Tenta converter a string para um objeto datetime
        data = datetime.strptime(data_str, '%d/%m/%Y')
        return True
    except ValueError:
        # Se ocorrer um ValueError, a data é inválida
        return False

data_input = input('Digite uma data no formato dd/mm/aaaa: ')

# Verifica se a data é válida
#O programa chama a função verificar_data com a data inserida pelo usuário. Dependendo do resultado, ele imprime se a data é válida ou inválida.

if verificar_data(data_input):
    print("A data é válida.")
else:
    print("A data é inválida.")