# constantes para valores fixos ao longo do programa
# C para caminhao e P/M/G para tamanhos
CP_VALOR = 4.87
CM_VALOR = 11.92
CG_VALOR = 27.44

CP_CARGA = 1
CM_CARGA = 4
CG_CARGA = 10

CELULAR = 0.5
GELADEIRA = 60
FREEZER = 100
CADEIRA = 5
LUMINARIA = 0.8
LAVADORA = 120

# Função para achar a distância dentro da matriz
def consultarTrecho(indexC, dados):
    # index 1 e 2 são as posições das cidades dentro da matriz
    index1 = indexC[0]
    index2 = indexC[1]
    
    del dados[0]
    trecho = dados[index1][index2]
    return trecho

# Função para achar o index das cidades dentro da matriz
# escolhi fazer separado caso precisasse chamar as funções separadamente
def consultarIndexCidade(dados, c):
    indexCidades = []
    # variavel Existe para verificar se a cidade consta na matriz
    existe = False
    cidade = dados[0]
    
    
    for i in range(2):
        for j in cidade:
            if j == c[i]:
                existe = True
                indexCidades.append(cidade.index(c[i]))
                break
            
    # caso não existe, retorna um array vazio
    if existe == False: return []
    trecho = consultarTrecho(indexCidades, dados)
            
    return trecho

arq = open("DNIT-Distancias.csv", "r")
dados = []
cidades = []
for linha in arq:
    dados.append(linha.split(";"))

opcao = 5 #ALTERAR DEPOIS
opcaoTransporte = 5


while opcao != 0:
    opcao = int(input("Digite a opção desejada:\n1 - Consultar trecho x modalidade\n2 - Cadastrar Transporte\n3 - Relatório\n0 - Finalizar programa\n"))
    # verificar o que foi digitado
    if ((opcao < 0 and opcao > 4) or (type(opcao) != int)):
        int(input("Valor inválido, favor digitar novamente."))
    else:
        if opcao == 1:
            cidades.append(input("Digite o estado que será ponto de partida sem acentuação:\n").upper())
            cidades.append(input("Digite o estado que será ponto de chegada sem acentuação:\n").upper())
            trecho = int(consultarIndexCidade(dados, cidades))
            
            # array vazio sendo varificado
            if not trecho:
                print("Cidade inválida.")
            else:
            
                while ((opcaoTransporte < 1) or (opcaoTransporte > 3)):
                    opcaoTransporte = int(input("Digite a opção de caminhão para o transporte:\n1 - Caminhão pequeno(4,87R$/km - 1T)\n2 - Caminhão médio(11,92R$/km - 4)\n3 - Caminhão grande(27,44R$/km - 10T)\n"))
                    
                    if opcaoTransporte == 1:
                        transporte_valor = CP_VALOR
                        transporte_caminhao = "caminhão pequeno"
                    elif opcaoTransporte == 2:
                        transporte_valor = CM_VALOR
                        transporte_caminhao = "caminhão médio"
                    elif opcaoTransporte == 3:
                        transporte_valor = CG_VALOR
                        transporte_caminhao = "caminhão grande"
                    else:
                        print("Opção inválida, digite novamente.")
                
                valorTotal = trecho * transporte_valor
                print(f"de {cidades[0]} para {cidades[1]}, utilizando um {transporte_caminhao}, a distância é de {trecho} km e o custo será de R$ {valorTotal}")
            
        elif opcao == 0:
            print("Encerrando.")