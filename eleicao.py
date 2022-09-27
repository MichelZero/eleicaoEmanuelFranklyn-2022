from candidato import Candidato
from eleitor import Eleitor
from voto import Voto
class Eleicao:
  def __init__(self):
    self.candidatos = []
    self.eleitores = []
    self.votos = []

  def perguntar(self, pergunta, opcoes):
    while True:
      perguntao = input(pergunta)
      perguntai = None
      try:
        perguntai = int(perguntao)
      except:
        print('Não foi possível processar sua entrada, tente novamente digitando um número.')
        continue
      if (opcoes != None):
        if (perguntai in opcoes):
          return perguntai
        else:
          print('Entrada invalida! Tente uma das opções disponiveis')
      else:
        return perguntai

  def menu(self):
    print('#---------------------------------')
    print('| Urna 1313 - Votações Eleitorais!')
    print('| Selecione uma opção:            ')
    print('| > 1 - Votar                     ')
    print('| > 2 - Cadastrar candidato       ')
    print('| > 3 - Encerrar votação          ')
    print('#---------------------------------')
    opcoes = self.perguntar("> Digite uma das Opções acima: \n> ", [1,2,3])
    
    if (opcoes == 1):
      return self.menuCpf()
    elif (opcoes == 2):
      return self.menuCadastrarCandidato()
    elif (opcoes == 3):
      return self.menuFinalizar()
    
  def menuCpf(self):
    print('#---------------------------------')
    print('| > 0 Para voltar')
    print('| > Digite o seu CPF (000.000.000-00):')
    cpf = input('| | > ')
    try:
      test = int(cpf)
      if (test == 0):
        print('#---------------------------------')
        return self.menu()
    except:
      pass
    found = False
    for eleitorTest in self.eleitores:
      if (eleitorTest.cpf == cpf):
        found = True
    if (found):
      print('| > Você já votou!')
      print('#---------------------------------')
      return self.menu()
    eleitor = Eleitor(cpf)
    self.eleitores.append(eleitor)
    print('#---------------------------------')
    return self.menuVotar(eleitor)
  
  def menuVotar(self, eleitor):
    print('#---------------------------------')
    print('| > 0 Para voltar')
    print('| > Digite o código do candidato:')
    possiveisNumeros = list(range(10,100))
    possiveisNumeros.append(0)
    candidato = self.perguntar('| | > ', possiveisNumeros)
    if (candidato == 0):
      print('#---------------------------------')
      return self.menu()
    else:
      nomeCandidato = None
      numeroCandidato = None
      for candidat in self.candidatos:
        if (candidat.numero == candidato):
          nomeCandidato = candidat.nome
          numeroCandidato = candidat.numero
          break
        
      if (numeroCandidato != None):
        votoCandidato = Voto(numeroCandidato, eleitor.cpf)
        self.votos.append(votoCandidato)
        print(f'Votado com sucesso em: {nomeCandidato}')
      else:
        votoNulo = Voto(0, eleitor.cpf)
        self.votos.append(votoNulo)
        print('Voto Nulo!')
    print('#---------------------------------')
    return self.menu()
  
  def menuCadastrarCandidato(self):
    print('#---------------------------------')
    print('| > 0 Para voltar')
    print('| > Digite o número do seu candidato:')
    possiveisNumeros = list(range(10,100))
    possiveisNumeros.append(0)
    numero = self.perguntar('| | > ', possiveisNumeros)
    if (numero == 0):
      print('#---------------------------------')
      return self.menu()
    for candids in self.candidatos:
      if (candids.numero == numero):
        print('| | > Um candidato com esse número já está cadastrado!')
        print('#---------------------------------')
        return self.menu()
    print('| > Por favor diga o nome do candidato:')
    nome = input('| | > ')
    print('| > Por favor diga o partido do candidato:')
    partido = input('| | > ')
    candidato = Candidato(nome, partido, numero)
    self.candidatos.append(candidato)
    print('| Candidato adicionado com sucesso!')
    print('#---------------------------------')
    return self.menu()
  
  def menuFinalizar(self):
    print('#---------------------------------')
    print('| Urna 1313 - Votações Eleitorais!')
    print('| Resultado da votação:')
    print('#---------------------------------')
    totalVotos = 0
    nulos = 0
    for voto in self.votos:
      totalVotos += 1
      if (voto.candidato == 0):
        nulos += 1
    print(f'| Total de votos: {totalVotos}')
    print(f'| Votos nulos: {nulos}')
    print(f'| - Candidatos e seus votos:')
    
    maxCand = self.candidatos[0]
    maxVotos = 0
    
    for cand in self.candidatos:
      votos = 0
      for voto in self.votos:
        if (cand.numero == voto.candidato):
          votos += 1
      if (maxVotos < votos):
        maxCand = cand
        maxVotos = votos
      print(f'| {cand.nome} - ${cand.numero} : {votos} votos # Partido: {cand.partido}')
    
    print('#---------------------------------')
    print('| Vencedor da eleição:')
    print(f'| {maxCand.nome} - ${maxCand.numero} : {maxVotos} votos # Partido: {maxCand.partido}')
            