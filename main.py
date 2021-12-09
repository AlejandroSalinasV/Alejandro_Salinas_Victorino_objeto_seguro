from proyecto import *

#  GENERAR OBJETOS
Alejandro = ObjetoSeguro("Alejandro")
BOB = ObjetoSeguro("BOB")
#  comunicacion ejemplo
print("SALUDAR")
mensaje_c = Alejandro.saludar("BOB", "Hola me llamo ALEJANDRO SALINAS")
BOB.esperar_respuesta(mensaje_c)
respuesta = BOB.responder("Alejandro")
Alejandro.esperar_respuesta(respuesta)

# Otros elementos para comprobar el registro de la comunicacion
print("COMPROBAR LA CONSULTA DE ARCHIVOS")
respuesta = BOB.responder("Alejandro")
Alejandro.esperar_respuesta(respuesta)
respuesta = BOB.responder("Alejandro")
Alejandro.esperar_respuesta(respuesta)

Alejandro.consultar_msj(2)
Alejandro.consultar_msj(1)
Alejandro.consultar_msj(0)
