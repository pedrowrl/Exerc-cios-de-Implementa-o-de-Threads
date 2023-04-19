#Aluno: Pedro Wilson Rodrigues de Lima.
#Nº de Matrícula: 2020267
#Data: 19/04/2023


#Exercício de criar 2 threads com números de 1 a 500 de forma crescente e decrescente:

import threading

def count_up():
    for i in range(1, 501):
        print(i)

def count_down():
    for i in range(500, 0, -1):
        print(i)

t1 = threading.Thread(target=count_up)
t2 = threading.Thread(target=count_down)

t1.start()
t2.start()

t1.join()
t2.join()
