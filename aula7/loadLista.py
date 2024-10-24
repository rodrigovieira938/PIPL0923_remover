import pickle

with open("saveList.pickle", "rb") as f:
    lista = pickle.load(f)
print(lista)