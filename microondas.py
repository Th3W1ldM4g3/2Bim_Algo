import time

ligado = False
tempo = 0
potencia = 0

def ligar(novo_tempo, nova_potencia):
    global ligado, tempo, potencia
    if not ligado:
        ligado = True
        tempo = novo_tempo
        potencia = nova_potencia
        print(f"Microondas ligado por {tempo} segundos na potência {potencia}")
        iniciar_cronometro(tempo)
        desligar()
    else:
        print("O microondas já está ligado")
        
def desligar():
    global ligado
    if ligado:
        ligado = False
        print("O microoondas foi desligado")
    else:
        print("O microondas já está desligado")
        
def status():
    if ligado:
        print(f"tempo: {tempo} segundos \n potência {potencia}")
    else:
        print("Desligado")
        
def iniciar_cronometro(segundos):
    while segundos > 0:
        print(f"Tempo restante: {segundos} segundos", end = "\r")
        
        time.sleep(1)
        segundos -= 1
    print("\n Tempo esgotado")
    
def pipoca():
    ligar(30, 100)

pipoca()