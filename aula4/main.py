








# list (arrays)
# sets
# None


# Dicionários e Funções
 
'''
[(k, v),(k, v),(k, v),(k, v)]
'''
 
'''
lista = []
set = {}
dict = {"key": "value"}     #Estrutura base do dicionário (dict)
'''
 
print("------"*4)
lista0 = ["Value1","Value2","Value3"]
print(lista0[0])
 
print("\n------"*4)
mySet = {"Value1","Value2","Value3"}
print(mySet)
 
print("\n------"*4)
infos = {"key": "value 1", "key2": "value 2", "key3": "value 3","key4": "value 4", "key5": "value 5"}
print(f"key: {infos["key"]}")
print(f"key2: {infos["key2"]}")
print(f"key3: {infos.get("key3")}")
 
print(f"key5: {infos.get("key5") is not None}")
print(f"key5: {infos.get("outra Key") is None}")
 
print(infos)
 
print("\n--- print(infos.keys()) ---")
print(infos.keys())
 
print("\n--- print(infos.values()) ---")
print(infos.values())
 
print("\n--- infos.items() ---")
print(infos.items())
 
print('key' in  infos)
print('key' in  infos.keys())
print('key' in  infos.values())
print(("key", "value 1" in  infos.items()))
 
print("\n------- Mudar valor -------")
 
print(infos.get("key"))
 
infos["key"] = "Novo Valor"
print(f"key: {infos["key"]}")
 
print("\n------- Adicionar valor -------")
 
print(infos)
 
infos["Nova Key"] = "Novo Valor 2"
print(infos)
 
print("\n------- Remover valor -------")
print(infos.keys())
 
infos.pop("Nova Key")
print(infos.keys())
 
del infos["key4"]
print(infos.keys())
 
infos.clear()       # -> Remove tudo o que está no dicionário
print(infos)
 
print("\n------- Dicionário V2 -------")
 
escola = "ATEC"
d1 = {"nome": "Suellen", "Escola": escola}
d2 = {"Turma1": "PIPL0923", "Turma2": "PIPL0922"}
 
print(f"d1           : {d1}")
print(f"d2           : {d2}")
d1.update(d2)
print(f"d1.update(d2): {d1}")
 
print("\n------- Loops lista -------")
 
lista = [1, 2, 3, 4, 5, 6, 7]
 
for i in lista:
    print(i)
   
print("\n------- Loops dict -------")
 
for i in d1:
    print(i)
 
print("-----")
for i in d1.keys():
    print(i)    # keys
 
print("-----")
for i in d1.keys():
    print(d1[i])    # Valores
   
print("--- for i in d1.keys(): ---")
for i in d1.keys():
    print(i)    # keys
 
print("--- for i in d1.values(): ---")
for i in d1.values():
    print(i)    # Valores