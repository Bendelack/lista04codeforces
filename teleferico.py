#pelo menos um monitor por viagem

capacidade = int(input())

alunos = int(input())
#total de viagens
if (alunos % (capacidade - 1)) == 0:
    print(int(alunos / (capacidade - 1)))
else:
    print((alunos//(capacidade - 1)) + 1)

#viagens = math.ceil(alunos/(capacidade - 1))
    
#print(viagens)