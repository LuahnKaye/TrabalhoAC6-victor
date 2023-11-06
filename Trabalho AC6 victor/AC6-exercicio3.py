from datetime import datetime
import locale

# Define o local para o português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def data_para_formato_extenso(data):
    try:
        data_obj = datetime.strptime(data, "%d/%m/%Y")
        formato_extenso = data_obj.strftime("%d de %B de %Y")
        return formato_extenso
    except ValueError:
        return None

# Solicita a entrada do usuário
data_input = input("Digite uma data no formato DD/MM/AAAA: ")

# Chama a função com a data inserida pelo usuário
data_formatada = data_para_formato_extenso(data_input)

# Verifica se a data é válida e imprime o resultado
if data_formatada:
    print(data_formatada)
else:
    print("Data inválida")