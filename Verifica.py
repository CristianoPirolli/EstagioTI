import re

def normalizar_numero(numero):
    return re.sub(r'[^0-9]', '', str(numero))

def identificar_anexo(numero):
    anexos = {
        "I": ["4729602", "4731800", "4732600", "4771701", "4771702", "4771703", "4771704", "4773300", "4774100", "4784900"],
        "II": ["4711301", "4711302", "4723700"],
        "III": ["4721102", "4772500", "5611201", "5611203", "5611204", "5611205"],
        "IV": ["4712100", "4721104", "4722901", "4724500", "4729699", "4741500", "4744001", "4744002", "4744003", "4744004", "4744005", "4744006",
               "4744099", "4754701", "4754702", "4789004"],
        "V": ["4511101", "4511102", "4530703", "4530705", "4541206", "4713002", "4713004", "4713005", "4781400", "4782201", "4782202", "4783101",
              "4783102", "4785701", "4785799", "4789001", "4789002", "4789003", "4789005", "4789006", "4789007", "4789008", "4789009"]
    }
    for anexo, lista in anexos.items():
        if numero in lista:
            return f"Código {numero} pertence ao Anexo {anexo}."
    return f"Código {numero} não pertence a nenhum anexo fornecido."

while True:
    numero_input = input("Digite o Código (ou 'sair' para encerrar): ")
    if numero_input.lower() == "sair":
        print("Encerrando o programa...")
        break
    
    numero_normalizado = normalizar_numero(numero_input)
    resultado = identificar_anexo(numero_normalizado)
    print(resultado)
