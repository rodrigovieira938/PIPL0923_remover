import pickle
from Pessoa import Pessoa

p = Pessoa("Rui", 23)

data = pickle.dumps(p)

#print(data)

myData = pickle.loads(data)

print("myData")
print(myData)