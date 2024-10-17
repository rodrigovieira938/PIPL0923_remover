# Crie a função -> sum_lista <- que conte quantas vezes as letra aparece num string
def quan_str(string:str):
    dic = {}
    for letra in string:
        if letra.isalpha():
            if dic.get(letra) != None:
                dic[letra] = dic[letra]+1
            else:
                dic[letra] = 1
    return dic
print(quan_str("aabbc"))