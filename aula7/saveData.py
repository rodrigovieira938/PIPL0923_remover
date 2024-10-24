from Pessoa import Pessoa
import pickle

print("--- Salva os dados ---")

p = Pessoa("Rui", 21)
print(p)

#Guarda em bin
file = open("Pessoa.pickle", "wb")
pickle.dump(p, file)
file.close()