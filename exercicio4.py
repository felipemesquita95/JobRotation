def exercicio4(estados, faturamentos):
    porcentagens = []
    total=0;

    for f in faturamentos:
        total+=f

    for f in faturamentos:
        porcentagens.append((100*f)/total)

    for i in range(len(porcentagens)):
        print(estados[i] + " - " + str(porcentagens[i]) + "%")


estados = ["SP", "RJ", "MG", "ES", "Outros"]
faturamentos = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]

exercicio4(estados, faturamentos)
