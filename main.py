import math
file = open('input.txt', "r")
l = open("output.txt", "w")
a = file.read().split(" ")
b = list(map(float,a))


def calc(n, p):
    h= (1/n)-math.exp(n)*math.sin(p)
    y= h/math.abs(h+1)
    return [n, p, h, y]
f = calc(b[0],b[1])
l.write(""+str(f[0])+" "+str(f[1])+" "+str(f[2])+" "+str(f[3]))
file.close()
l.close()

