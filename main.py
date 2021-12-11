from proyecto import *

"""
PYTHON & LINUX. CURSOS DE TALENTO ESPECIALIZADO EN CIBERSEGURIDAD
---	PROYECTO PARTE 1. OBJETO SEGURO	---
ALEJANDRO SALINAS VICTORINO
"""

#  GENERAR OBJETOS
Alejandro = ObjetoSeguro("Alejandro")
Bob = ObjetoSeguro("Bob")

#  INTERCAMBIO DE LLAVES
print("[0] Intercambio de llaves entre objetos")
Alejandro.monedero_llaves_pub(Bob.nombre, Bob.llave_publica())
Bob.monedero_llaves_pub(Alejandro.nombre, Alejandro.llave_publica())

#  COMUNICACION DE EJEMPLO
print("[1] Alejandro saluda a Bob")
mensaje_c = Alejandro.saludar("Bob", "Hola me llamo Alejandro Salinas")

# Bob recibe el saludo de alejandro, y contesta automaticamente 
print("[2 & 3]  Bob recibe el saludo de Alejandro, y contesta automaticamente")
respuesta = Bob.esperar_respuesta(mensaje_c)

# Alejandro recibe la respuesta
print("[4] Alejandro recibe la respuesta")
Alejandro.esperar_respuesta(respuesta)


# siguimiento de la charla
print("\n\t[...] Continuacion de la comunicacion [...]\n")
print("[...] Alejandro le contesta a Bob")
respuesta2 = Alejandro.responder("Espero que te encuentres bien")
print("[...] Bob espera la respuesta")
Bob.esperar_respuesta(respuesta2)
print("[...] Bob le contesta a Alejandro")
respuesta3 = Bob.responder("Claro que me encuentro bien. Salu2")
print("[...] Alejandro espera la respuesta")
Alejandro.esperar_respuesta(respuesta3)

# Otros elementos para comprobar el registro de la comunicacion
print("\n\t---COMPROBAR LA CONSULTA DE ARCHIVOS---")
print(f"Mensajes recibidos de {Alejandro.nombre}")
Alejandro.consultar_msj(0)
Alejandro.consultar_msj(1)
Alejandro.consultar_msj(2)  # en caso de que no exista dicha linea, no retorna nada
Alejandro.consultar_msj(3)

print("--------------------\t----------------------")
print(f"Mensajes recibidos de {Bob.nombre}")
Bob.consultar_msj(0)
Bob.consultar_msj(1)
