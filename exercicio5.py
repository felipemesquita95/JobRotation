def exercicio5(palavra):
    reversa = "" ;
    for i in range(len(palavra)-1, -1, -1):
        reversa = reversa + palavra[i];

    return reversa

print(exercicio5("exercicios"))
