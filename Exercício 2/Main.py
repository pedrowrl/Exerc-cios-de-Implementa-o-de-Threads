#Aluno: Pedro Wilson Rodrigues de Lima.
#Nº de Matrícula: 2020267
#Data: 19/04/2023


#Exercício de implentação de um programa em Python que realiza o cálculo das somas dos valores das linhas de uma matriz 5x5:

import threading
import random

matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]

result = [0]*5

def calculate_sum(row):
    result[row] = sum(matrix[row])

threads = []
for row in range(5):
    thread = threading.Thread(target=calculate_sum, args=(row,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

for row, sum in enumerate(result):
    print(f"Soma da linha {row+1}: {sum}")