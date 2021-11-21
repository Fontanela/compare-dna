print("Henrique dos Santos Hernandes NºUSP: 11779754\nGabriel Patrocinio Garicoix Proença NºUSP: 11845323\n")
#Inclusão das bibliotecas necessárias 
from collections import Counter

#Definição da função para leitura
def read_fasta(arq):
 seq = ''
 with open(arq) as f:
   f.readline()
   for line in f:
     seq += line.strip()
 return seq

#Definição da função para determianr o numero total de aminoacidos
def aatotal(seqanimal):
  numero = 0
  for element in seqanimal:
    numero += 1
  return numero

#Conversão dos arquivos .fasta para variáveis  
cavalo = './docs/horse.fasta'
hamster = './docs/hamster.fasta'
rato = './docs/rat.fasta'

#Variaveis a partir da leitura dos arquivos
seqcavalo = read_fasta(cavalo)
seqhamster = read_fasta(hamster)
seqrato = read_fasta(rato)

#Total do numero de aminoácidos para cada um dos organismos
totalcavalo = aatotal(seqcavalo)
totalhamster = aatotal(seqhamster)
totalrato = aatotal(seqrato) 

if totalcavalo == totalhamster == totalrato:
  print("Todas as sequências possuem o mesmo comprimento.\n")
else:
  print("As sequências não possuem o mesmo tamanho\n")

totalaa = totalcavalo #Variavel para o número total de atributos, visto que as três sequências tem o mesmo tamanho

#Converte a sequencia de aminoacidos em dicionarios 
aacavalo = Counter(seqcavalo)
aahamster = Counter(seqhamster)
aarato = Counter(seqrato)

#Função que estabelece uma variavel para a quantidade de aminoacidos no dicionario e faz a diferença entre esses valores
def diferenca(aminoacido1, aminoacido2):
 totaldif = 0
 for key in aminoacido1:
     totaldif += abs(aminoacido1[key] - aminoacido2[key])
 return(totaldif)

#A comparação entre três pares de organismos
difcavham = diferenca(aacavalo, aahamster)
difcavrat = diferenca(aacavalo, aarato)
difratham = diferenca(aarato, aahamster)

#Resolução do primeiro tópico sobre verificação simples
#Função que define a formula da variaçao simples 
def variacao_simples(difanimal):
  valores_iguais = totalaa - difanimal
  resposta = (totalaa - valores_iguais)/totalaa
  return(resposta)

print("A variação simples entre o cavalo e o hamster é:" ,variacao_simples(difcavham))
print("A variação simples entre o cavalo e o rato é:" ,variacao_simples(difcavrat))
print("A variação simples entre o rato e o hamster é:" ,variacao_simples(difratham))