#Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях(не индексах).
import random
n=random.randint(1,5)
roster=list()
for i in range(-n, n+1):
    roster.append(i)
print(roster)
a=int(input('input number 1: '))
b=int(input('input number 2: '))
for z in range (len(roster)):
    if z==a-1:
        c=roster[a-1]
for y in range (len(roster)):
    if y==b-1:
        d=roster[b-1]
print (f'{c} , {d}')
print(f'{c*d}')

