Animales = ["perro","gato","serpiente"]
animalito = ["perra","gata","pata"]

for num, valor in enumerate(zip(Animales,animalito)):
    if num == 0: 
        print("hola buenos dias")
        continue
    else: print("no ha pasado nada hijo")
    print(valor)
    print(num)
    

diccionario = {
    "nombre": "Jhon",
    "apellido": "Ochoa",
    "edad"  : 18
 }

for dict, doct in diccionario.items(): 
    print(dict)
    print(doct)