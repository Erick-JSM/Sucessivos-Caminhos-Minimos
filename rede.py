class Rede:
  import csv
  import pandas as pd

  
  """usar 3 matrizes uma de adj( binaria), de pesos( float) e de capacidades ( float)"""

  def __init__(self, num_vert = 0, num_arestas = 0, mat_adj = None, mat_pesos = None, mat_capacidade = None, vet_demanda = None, lista_adj = None, dicionario = {0 : "s"}):
    
    self.num_vert = num_vert
    self.mat_adj = mat_adj
    self.mat_capacidade = mat_capacidade
    self.mat_pesos = mat_pesos
    self.vet_demanda = vet_demanda
    self.dicionario = dicionario
    self.num_arestas = num_arestas
    self.preferencia = {1:0, 2:3, 3:5, 4:8 ,5:10}
    
    """Matriz de adjacencia binaria"""
    if mat_adj is None:
      self.mat_adj = [[0 for j in range(num_vert)] for i in range(num_vert)]
    else:
      self.mat_adj = mat_adj
      
    """Matriz de pesos"""
    if mat_pesos is None:
      self.mat_pesos = [[0.0 for j in range(num_vert)] for i in range(num_vert)]
    else:
      self.mat_pesos = mat_pesos
      
    """Matriz de capacidades"""
    if mat_capacidade is None:
      self.mat_capacidade = [[0.0 for j in range(num_vert)] for i in range(num_vert)]
    else:
      self.mat_capacidade = mat_capacidade
      
    """Vetor de demanda"""
    if mat_capacidade is None:
      self.vet_demanda = [[] for i in range(num_vert)]
    else:
      self.vet_demanda = vet_demanda
    """Dicionario"""
    if dicionario is None:
      self.dicionario = [[]for i in range(num_vert)]
    else:
      self.dicionario = dicionario
    """Lista de adjacencia"""
    if lista_adj is None:
      self.lista_adj = [[] for i in range(num_vert)]
    else:
      self.lista_adj = lista_adj

#====================================================================================================================
  def cria_dic (self, lista, lista2):
    cont = 1
    index = 0
    

    for i in range(len(lista)):
      for j in lista[i]:
        aux = {cont:j}
        self.dicionario.update(aux)
        cont += 1
        marcador = cont
        break
        
    for i in range(len(lista2)):
      for j in lista2[i]:
        aux = {cont:j}
        self.dicionario.update(aux)
        cont += 1
        index += lista2[i][2]
        break

    aux = {cont: "t"}
    self.dicionario.update(aux)
    self.num_vert = cont + 1
    
    self.mat_adj = [[0 for j in range(self.num_vert)] for i in range(self.num_vert)]
    self.mat_pesos = [[float("inf") for j in range(self.num_vert)] for i in range(self.num_vert)]
    self.mat_capacidade = [[0.0 for j in range(self.num_vert)] for i in range(self.num_vert)]
    self.vet_demanda =  [[]for j in range(self.num_vert)]
    self.vet_demanda[0] = index
    self.vet_demanda[self.num_vert-1] = -index
    self.lista_adj = [[] for i in range(self.num_vert)]
    
    linha = 0
    coluna = 1
    
    for tupla in lista:
      if coluna < marcador and coluna !=0 and linha == 0:
        self.mat_adj[linha][coluna] = 1
        self.mat_capacidade[linha][coluna] = tupla[1]
        self.add_aresta(linha,coluna, 0)
      coluna = coluna + 1
      
    linha += 1
    for tupla in lista:
      coluna = marcador
      while coluna != self.num_vert - 1 and linha > 0 and linha <= marcador:
        
        if tupla[2] == self.dicionario.get(coluna):
          self.mat_adj[linha][coluna] = 1
          self.mat_capacidade[linha][coluna] = float("inf")
          self.mat_pesos[linha][coluna] = self.preferencia.get(1)
          self.add_aresta(linha,coluna, self.preferencia.get(1))
          
        elif tupla[3] == self.dicionario.get(coluna):
          self.mat_adj[linha][coluna] = 1
          self.mat_capacidade[linha][coluna] = float("inf")
          self.mat_pesos[linha][coluna] = self.preferencia.get(2)
          self.add_aresta(linha,coluna, self.preferencia.get(2))
          
        elif tupla[4] == self.dicionario.get(coluna):
          self.mat_adj[linha][coluna] = 1
          self.mat_capacidade[linha][coluna] = float("inf")
          self.mat_pesos[linha][coluna] = self.preferencia.get(3)
          self.add_aresta(linha,coluna, self.preferencia.get(3))
          
        elif tupla[5] == self.dicionario.get(coluna):
          self.mat_adj[linha][coluna] = 1
          self.mat_capacidade[linha][coluna] = float("inf")
          self.mat_pesos[linha][coluna] = self.preferencia.get(4)
          self.add_aresta(linha,coluna, self.preferencia.get(4))
          
        elif tupla[6] == self.dicionario.get(coluna):
          self.mat_adj[linha][coluna] = 1
          self.mat_capacidade[linha][coluna] = float("inf")
          self.mat_pesos[linha][coluna] = self.preferencia.get(5)
          self.add_aresta(linha,coluna, self.preferencia.get(5))
          
          
        coluna += 1
      linha += 1

    coluna = self.num_vert-1
    linha = marcador
    for tupla in lista2:
      if linha != self.num_vert-1 and linha != coluna:
        self.mat_adj[linha][coluna] = 1
        self.mat_capacidade[linha][coluna] = tupla[2]
        self.add_aresta(linha,coluna, 0)
      linha += 1
    
#====================================================================================================================    
  def add_aresta(self, u, v, w = 1):
    """Adiciona aresta de u a v com peso w"""
    if u < self.num_vert and v < self.num_vert:
      self.num_arestas += 1
      self.lista_adj[u].append((v, w))
    else:
      print("Aresta invalida!")
      
#====================================================================================================================     
  def sucessivos_caminhos_min(self):
    s = 0
    t = self.num_vert-1
    F = [[0 for j in range(self.num_vert)] for i in range(self.num_vert)]
    C = self.bellman_ford(s, t)
    
    while len(C) != 0 and self.vet_demanda[0] > 0:
      f = float('inf')
      for i in range(1, len(C)):
        u = C[i-1]
        v = C[i]
        if self.mat_capacidade[u][v] < f:
          f = self.mat_capacidade[u][v]
  
      for i in range(1, len(C)):
        u = C[i-1]
        v = C[i]
        
        F[u][v] += f
        self.mat_capacidade[u][v] = self.mat_capacidade[u][v] - f
        
        if self.mat_capacidade[u][v] == 0:
          self.mat_adj[u][v] = 0
          self.mat_pesos[u][v] = float("inf")
          self.lista_adj[u].remove((v, self.mat_capacidade[u][v]))
          

        if self.mat_adj[v][u] == 0:
          self.mat_adj[v][u] = 1
          self.mat_pesos[v][u] = -(self.mat_pesos[u][v])
          self.mat_pesos[u][v] = float("inf")
          
        if F[v][u] != 0:
          F[v][u] -= f
          
      self.vet_demanda[s] -= f
      self.vet_demanda[t] += f
      C = self.bellman_ford(s, t)
    self.imprimeDados(F)
#====================================================================================================================    
  def imprimeDados(self, F):
    for i in range(len(F)):
      for j in range(len(F)):
        if i != 0 and F[i][j] != 0 and j != len(F)-1:
          print(self.dicionario.get(i), "     |   ", self.dicionario.get(j), "  |  ", F[i][j], "  |  ", -self.mat_pesos[j][i])
        
          
          
#====================================================================================================================     
  def bellman_ford(self, s, t):
  
    pred = [None for v in range(self.num_vert)]  # Vetor que guarda os predecessores
    dist = [float("inf") for v in range(self.num_vert)]   # Vetor que guarda a distancia
    dist[s] = 0  # Marca o vertice na posição s com distancia 0

    caminho = []
    count = t

    for i in range(self.num_vert-1):
      flag = False
      for u in range(self.num_vert):
        for v,w in self.lista_adj[u]:  # Compara o peso da aresta u e v
          if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            pred[v] = u
            flag = True
      if flag == False:  # Encerra o laço prematuramente
        break
  
    i = -1
    caminho.append(t)
    while i != s:
      if pred[count] != None:
        i = pred[count]
        count = i
        caminho.append(i)
      else:
        break

    caminho.reverse()
    return caminho
  
#====================================================================================================================     
  def ler_arquivo(self, nome_arq, nome_arq2):
    import pandas as pd
    """Le um arquivo"""
    try:
      """Leitura do cabeçalho"""
      arq = pd.read_csv(nome_arq, sep = ';')
      arq2 = pd.read_csv(nome_arq2, sep = ';')
      lista = arq.values.tolist()
      lista2 = arq2.values.tolist()

      self.cria_dic(lista, lista2)
      
    except IOError:
      print("Nao foi possivel encontar o arquivo!")
      
#====================================================================================================================  