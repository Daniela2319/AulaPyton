import time

<<<<<<< HEAD:aula5.py
#Primeira maneira 
=======
#Primeira maneira
>>>>>>> 5ed0e1bb3ff17a40e9437d23212d0114d72a26c3:Proz-Talento-AWS-Nexa/projetoEstruturaRepetição.py
andar_inicial = 20
andar_final = 0

# andar e descrescente na estrutura repetição for
print('Iniciando a descida!')

for i in range(andar_inicial, andar_final, -1):
  if (i == 13): #enquanto o andar está descendo para no 13° andar 
     continue       #continue no proxímo andar.
  print(i)
  time.sleep(1)
  print(f'Chegou na sua parada {i}')

<<<<<<< HEAD:aula5.py
 
#segunda maneira
for andar in range(21, 0, -1):
    if andar != 13:
        print(andar)


#terceira maneira
andar = 1
=======
#Segunda maneira
  andar = 1
>>>>>>> 5ed0e1bb3ff17a40e9437d23212d0114d72a26c3:Proz-Talento-AWS-Nexa/projetoEstruturaRepetição.py
while True:
    if andar != 13:
        print(andar)
    andar += 1
    if andar > 20:
        break
<<<<<<< HEAD:aula5.py
=======
print('***************************************')
    
#Terceira maneira
for andar in range(20, 0, -1):
    if andar != 13:
        print(andar)
>>>>>>> 5ed0e1bb3ff17a40e9437d23212d0114d72a26c3:Proz-Talento-AWS-Nexa/projetoEstruturaRepetição.py
