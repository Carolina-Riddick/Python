from ast import Break


while True:  
    anio = int(input("ingrese un año: "))  
if anio % 100 == 0:  
    	print("Bisiesto")  
elif anio % 4 != 0:  
    	print("No es Bisiesto.")  
else:  
      	anio % 400 != 0  
print("El año es Bisiesto")  
seguir = input("Desea continuar? ")  
if seguir == "no": 
    Break
