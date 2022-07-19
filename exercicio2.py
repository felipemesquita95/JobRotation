def exercicio2(numero):
    fib = [0, 1]
    
    if numero==0:
        return "Está Contido";
    elif numero==1:
        return "Está Contido";
    else:
        i=2;

        while i<numero:
            fib.append(fib[i-2]+fib[i-1]);
            i+=1;

    if numero in fib:
        return "Está contido"
    else:
        return "Não está contido"
