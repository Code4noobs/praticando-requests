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

