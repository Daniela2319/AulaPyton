import time

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

 