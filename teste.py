import requests

i = raw_input("site:")
	
meth = int(raw_input("""Escolha o metodo que deseja:
	[1] Para GET
	[2] Para POST
	[3] Para ver o Codigo Fonte """))
i2 = requests.get(i)
if meth == 1:

	print i2
elif meth == 2:
	print requests.post(i)
elif meth == 3:
	print i2.text
elif meth > 3:
	print "Numero MAIOR que o pedido"
elif meth < 1:
	print "Numero MENOR que o pedido"
