
def calculadora_imc(pessoa): 
    imc = pessoa["peso"] / (pessoa["altura"] * pessoa["altura"])
    resultado = f"o IMC {pessoa["nome"]} é {imc:.2f}"

    # comando ternario:
    saudavel = 18.5 < imc < 25 
    return {
        "nome": pessoa["nome"], 
        "imc": imc, 
        "resultado": resultado,
        "saudavel": saudavel
    } 

pessoa1={
    "nome": "josé", 
    "peso": 68,
    "altura": 1.65

}

print(calculadora_imc(pessoa1))