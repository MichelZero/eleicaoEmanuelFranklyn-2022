import time

class Voto:
  def __init__(self, candidato, cpf):
     timer = time.ctime().split(' ')
     date = timer[0:3]
     date.append(timer[-1])
     hora = timer[3]
     self.candidato = candidato
     self.cpf = cpf
     self.data = date
     self.hora = hora
     self.candidato = candidato

      