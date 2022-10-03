import utilidades as utils

funcionesUtilidades = ["",lambda: utils.crearBaseDatos(),lambda: utils.dropDatabase()]

def funcionParaLlamar (numero):
    numero = int(numero)
    if numero == 0:
        exit()
    if numero >= len(funcionesUtilidades):
        print("Error01: Ese numero es muy grande")
    else:
        return funcionesUtilidades[numero]()