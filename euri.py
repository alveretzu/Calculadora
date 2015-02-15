#Principal
import luis
import freddy
def main():
	print "esta es la calculadora \"Gevato\""
	opcion=input("deseas 1-sumar 2-restar 3-dividir 4-multiplicar o 5-salir")
	luis=input("ingrese el primer valor")
	freddy=input("ingrese el segundo valor")
	if opcion ==1:
		freddy.suma(luis,freddy)
	if opcion ==2:
		freddy.resta(luis,freddy)
	if opcion ==3:
		luis.multiplicacion(luis,freddy)
	if opcion ==4:
		luis.dividir(luis,freddy)
main() 
input()