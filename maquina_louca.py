import time

ligado = False
tempo = 0
temperatura = 0

def desligar():
    global ligado
    if ligado:
        ligado = False
        print("A lava-louças foi desligada")
    else:
        print("A lava-louças já está desligada")
        
def status():
    if ligado:
        print(f"tempo: {tempo} segundos \n temperatura {temperatura}°c")
    else:
        print("Desligado")
        
def iniciar_cronometro(segundos):
    while segundos > 0:
        print(f"Tempo restante: {segundos} segundos", end = "\r")
        
        time.sleep(1)
        segundos -= 1
    print("\n Tempo esgotado")
    
def ligar(novo_tempo, nova_temperatura):
    global ligado, temperatura, tempo
    if not ligado:
        ligado = True
        tempo = novo_tempo
        temperatura = nova_temperatura
        print(f"Lava-louças ligada por {tempo} segundos na temperatura {temperatura}°c")
        iniciar_cronometro(tempo)
        desligar()
    else:
        print("A lava-louças já está ligada")
    
def vidro():
    ligar(120, 100)

def plastico():
    ligar(60, 21)
    
def metal():
    ligar(120, 30)

escolha = input("Insira o tipo de material que quer lavar: ")
if escolha == "vidro":
    vidro()
elif escolha == "plástico":
    plastico()
elif escolha == "metal":
    metal()
else:
    print("Erro")