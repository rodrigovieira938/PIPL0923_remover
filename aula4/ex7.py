def quant_palavras(string:str):
    words = string.split(" ")
    dic = {}
    for word in words:
        if dic.get(word) != None:
            dic[word] = dic[word]+1
        else:
            dic[word] = 1
    return dic
res = quant_palavras("ola ola mundo mundo xj6")
print(res)