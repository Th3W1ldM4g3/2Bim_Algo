codigo = ("ABC123", "XYZ789", "DEF456", "JKL321", "MNO654", "PQR987", "STUU741") 
status = ("Enviado", "Recebido", "Em trânsito", "Enviado", "Recebido", "Em trânsito", "Enviado")


print('Utilizando "Count", mostraremos quantos pacotes foram enviados: ', status.count("Enviado"), ', estão em trânsito: ', status.count("Em trânsito"), ', e foram recebidos: ', status.count("Recebido"))

print('Utilizando "for" e "if", encontraremos os códigos cujos status são "Em trânsito" : ')
for i in range(len(codigo)):
    if status[i] == "Em trânsito":
        print(codigo[i])

print('Utilizando "index", encontraremos o status do pedido inserido, e utilizando "if" e "in", verificaremos se o pedido existe.')
pedido = input('Insira o código do seu pedido: ')
if pedido in codigo:
    print(status[codigo.index(pedido)])
else:
    print("Pedido não existe")

print('Utilizando "sorted", mostraremos os códigos de forma ordenada: ')
print(sorted(codigo))
