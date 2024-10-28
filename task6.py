# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное и максимальное из введённых чисел.
mas=[]
while True:
    x=int(input())
    if x==0:
          break
    else:
        mas.append(x)
if mas==[]:
    print("")
else:
    print(min(mas), max(mas))
