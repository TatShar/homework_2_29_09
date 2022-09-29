#3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
#Для n = 6: [2, 2, 2, 2, 2, 3] -> 13
import random
n = random.randint(1,10)
print(n)
ran = list()

for i in range(1,n+1):
    ran.append(round((1+1/i)**i))
print(ran)
y=0
sum=0
for z in range(1,n+1):
    sum=sum+ran[y]
    y+=1
print(sum)