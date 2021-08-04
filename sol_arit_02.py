#x = int(input())
x=49
sq_init = x
limite_valor = 10
for i in range (1,x+1):
    if i > limite_valor:
        continue
    print("N[{}] = {}".format(i-1, sq_init))
    sq_init *= 2