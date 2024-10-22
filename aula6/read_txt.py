f = open("demo.txt", "rt")



#print(f.read().split("\n"))



#print(f.read(3))
#print(f.read(4))



#print(f.readline()[0:-1]) # nao dá print para a nova linha que já existe na string
#print(f.readline()[0:-1])

for i in f:
    i = i[0:-1]
    print(i)