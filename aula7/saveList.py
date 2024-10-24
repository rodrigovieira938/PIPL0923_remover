from Pessoa import Pessoa
import pickle

print("--- Salva os dadoss ---")

lista = [
    Pessoa("Rui", 21),
    Pessoa("Ana", 31),
    Pessoa("Luis", 15)
    ]

with open("saveList.pickle", "wb") as f:
    pickle.dump(lista, f)