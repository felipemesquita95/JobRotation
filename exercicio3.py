def menorValor(dados):
    menor = dados[0]["valor"] ;
    it = 0;
    finalDeSemana = [4,5];
    aux=0;
    
    for i in range(len(dados)):
        if dados[i]["dia"] - (aux*7) == finalDeSemana[0]:
            aux = aux;
        elif dados[i]["dia"] - (aux*7) == finalDeSemana[1]:
            aux+=1;
        else:
            if dados[i]["valor"] < menor:
                menor = dados[i]["valor"]
                it = i;
    print("O menor valor de faturamento é do dia " + str(dados[it]["dia"]) + " e o valor é de R$" + str(dados[it]["valor"]) +".")
    return 

def maiorValor(dados):
    maior = dados[0]["valor"] ;
    it = 0;
    finalDeSemana = [4,5];
    aux=0;
    
    for i in range(len(dados)):
        if (dados[i]["dia"] - (aux*7)) == finalDeSemana[0]:
            aux = aux;
        elif dados[i]["dia"] - (aux*7) == finalDeSemana[1]:
            aux+=1;
        else:
            if dados[i]["valor"] > maior:
                maior = dados[i]["valor"]
                it = i;
    print("O maior valor de faturamento é do dia " + str(dados[it]["dia"]) + " e o valor é de R$" + str(dados[it]["valor"]) +".")
    return 

def mediaFaturamento(dados):
    total = 0;
    dias = 0;
    finalDeSemana = [4,5];
    aux=0;
    
    for i in range(len(dados)):
        if dados[i]["dia"] - (aux*7) == finalDeSemana[0]:
            aux = aux;
        elif dados[i]["dia"] - (aux*7) == finalDeSemana[1]:
            aux+=1;
        else:
            total+=dados[i]["valor"]
            dias+=1;
    print("A média mensal de faturamento nos dias úteis é de R$" + str(total/dias) +".")
    return     


    
import json

total1 =0 ;

with open("dados.json") as dados_json:
    dados = json.load(dados_json);
    
    for d in dados:
        total1+=d["valor"]
    
menorValor(dados)
maiorValor(dados)
mediaFaturamento(dados)




