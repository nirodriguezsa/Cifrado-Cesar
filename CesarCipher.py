# Codigo creado por Nicolas Rodriguez
# Este codigo no cifra espacios ni caracteres especiales. Para que lo haga, modifique el alfabeto de entrada y adicione los que crea pertinentes
# Si se llega a introducir un caracter especial (numeros, espacios, signos de admiracion, etc) el sistema no los va a cifrar y los iprimirá.

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
accion = "n" # Se inicializa en cualquier valor para que pueda entrar al while

def encriptar(mensaje,llave):
  estring = ""
  for letra in mensaje:
    if letra in alfabeto:
      estring = estring + alfabeto[(alfabeto.find(letra)+llave) % len(alfabeto)]  # concatena la cadena con la letra y su corrimiento modular del tamaño del alfabeto
    else: estring = estring + letra  #Se hace para no encriptar caracteres especiales ni espacios
  return estring

def desencriptar(mensaje,llave):
  estring = ""
  for letra in mensaje:
    if letra in alfabeto:
      estring = estring + alfabeto[(alfabeto.find(letra)-llave) % len(alfabeto) ]   # concatena la cadena con la letra y su corrimiento modular del tamaño del alfabeto
    else: estring = estring + letra  #Se hace para no encriptar caracteres especiales ni espacios
  return estring

while(accion != "s"):

  accion = (input("Escriba (c) para cifrar o (d) para decifrar un mensaje: ")).lower()

  if(accion == "c" or accion == "d"):

    mensaje = input("Ingrese el texto:    ").upper()
    llave = int(input("Ingrese numero de corrimientos:   "))

    if(accion == "c"):
      cifrado = encriptar(mensaje, llave)
      print(cifrado)


    elif(accion == "d"):
      descifrado = desencriptar(mensaje,llave)
      print(descifrado)#JVTV LZ JVTV ZLYPH

  elif(accion == "s"):
    print("Gracias utilizar por mi codigo de cifrado")

  else:
    print("¡ERROR! Ingrese (c) o (d) para arrancar el programa, para salir escriba (s)")