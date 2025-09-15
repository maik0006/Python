#Convertir un diccionario a lista de tuplas y viceversa
dic4 = {"a": 1, "b": 2, "c": 3}
tuplas = list(dic4.items())
print(tuplas)
nuevo_dic = dict(tuplas)
print(nuevo_dic)