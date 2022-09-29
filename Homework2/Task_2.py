#2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
#- 4 -> [1, 2, 6, 24]
#- 6 -> [1, 2, 6, 24, 120, 720

n= int(input('input a namber '))
ran = list()
for i in range(n):
    ran.append(i+1)
print(ran)
print ('schet')
res=list()
y=1
for z in range (1,n+1):
    res.append(z*y)
    y=z*y
print(res)

