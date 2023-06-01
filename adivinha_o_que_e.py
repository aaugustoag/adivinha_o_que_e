dicionario={'rei': ['homem','coroa','trono'],
            'rainha': ['mulher','coroa','trono'],
            'abacaxi': ['fruta','coroa','espinho'],
            'leao': ['animal','coroa','selva']}

def advinha(sentenca,dicionario):
    print(sentenca)
    sentenca_split = sentenca.split()
    resposta=[]
    if sentenca_split[0] in dicionario:
        item=dicionario[sentenca_split[0]].copy()
        for i, palavra in enumerate(sentenca_split):
            if palavra == "menos":
                item.remove(sentenca_split[i+1])
            if palavra == "mais":
                item.append(sentenca_split[i+1])
    else:
        item=[]
        for i, palavra in enumerate(sentenca_split):
            if palavra in ["é","tem"]:
                item.append(sentenca_split[i+1])
            if palavra in ["esta"]:
                item.append(sentenca_split[i+2])

    for palavra in dicionario:
        contador=0
        for caracteristica_item in item:
            if not(caracteristica_item in dicionario[palavra]):
                break
            else:
                contador+=1
            if contador == len(item):
                resposta.append(palavra)
    return resposta

sentenca="rainha menos mulher mais homem"
print(advinha(sentenca,dicionario))

sentenca="rainha menos coroa"
print(advinha(sentenca,dicionario))

sentenca="rainha menos mulher"
print(advinha(sentenca,dicionario))

sentenca="rainha menos mulher menos trono"
print(advinha(sentenca,dicionario))

sentenca="rainha menos mulher menos trono mais espinho"
print(advinha(sentenca,dicionario))

sentenca="tem coroa é mulher"
print(advinha(sentenca,dicionario))

sentenca="tem coroa esta na selva"
print(advinha(sentenca,dicionario))