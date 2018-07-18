import requests
i = str(raw_input("Site: "))
if i == "":
	print "Caracteres Nao validos"
	

i2 = input("""
Escolha o numero 
[*]1 para GET
[*]2 para POST:")
 
if i2 == "":
 	print "Numeros nao validos"
 	
elif i2 > 2:
	print "Numeros nao validos"
elif i2 < 1:
	print "numero nao validos"

g = requests.get(i)
p = requests.post(i)
s = g.status_code
s2 = p.status_code

if i2 == 1:
	print g
	print "O servidor deu", (s)
if i2 == 2:
	print p
	print "O servidor deu", (s2)
---------------------
#OUTRO CODIGO
import requests

i = raw_input("site:")
	
meth = int(raw_input("""Escolha o metodo que deseja:
	[1] Para GET
	[2] Para POST
	[3] Para ver o Codigo Fonte """))
if meth == 1:
	print requests.get(i)
elif meth == 2:
	print requests.post(i)
elif meth == 3:
	i.text
elif meth > 3:
	print "Numero MAIOR que o pedido"
elif meth < 1:
	print "Numero MENOR que o pedido"


