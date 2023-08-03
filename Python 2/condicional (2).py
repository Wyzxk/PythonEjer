contraseña = input("Registra tu contraseña")
Ingr_contra = None

def registrar():
    global Ingr_contra
    Ingr_contra = input("Escribe la contraseña")
    if contraseña == Ingr_contra:
        print("Has escrito la contraseña correctamente")
        
    else:
        print("Has escrito la contraseña incorrectamente, vuelvelo a intentar")
        registrar()
    



