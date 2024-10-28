# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить минимальное и максимальное среди двузначных чисел,
# которые делятся на 3. Если таких чисел не было, вывести "нет".
mas=[]
N=int(input())
for i in range(N):
    x=int(input())
    if len(str(x))==2 and x%3==0:
        mas.append(x)
if mas==[]:
    print("no")
else:
    print(min(mas),max(mas))
