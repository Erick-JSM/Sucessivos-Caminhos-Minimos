import rede

# redeEx = rede.Rede()
# redeEx.ler_arquivo("professores_toy.csv", "disciplinas_toy.csv")
# redeEx.sucessivos_caminhos_min()
redeEx = rede.Rede()
redeEx.ler_arquivo("professores.csv", "disciplinas.csv")
redeEx.sucessivos_caminhos_min()