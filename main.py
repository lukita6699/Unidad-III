#crear archivo, w es permiso de escritura
#Las comillas al inicio y 3 al final del texto representan un texto
#con saltos de línea

datos = """ Este es un archivo de texto simple que no tiene
ningún formato en particular, lo podemos utilizar
para guardar todo tipo de texto.

#Crear un contexto para abrir un nuevo archivo .txt
with open('archivo_nuevo.txt', 'w', encoding='utf-8') as archivo:
    archivo.write(datos);
print ("Se creo el archivo correctamente!"); 

#Crear un contexto para leer los datos de un archivo .txt
with open('archivo_nuevo.txt','r', encoding='utf-8') as archivo:
    print (archivo.read()); 

import csv
lista=['NOMBRE', 'EDAD', 'COMUNA'];
#Las filas de la tabla
matriz=[   
    ['Lucas', 18, 'Llanquihue'],
    ['Axel', 18, 'Llanquihue'],
    ['Mati Perro Flaco', 104, 'Puerto Montt']
    ]

#Crear el contexto para abrir un nuevo archivo .csv
with open('nuevo_archivo.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
# Escribir una fila en el archivo CSV
    escritor_csv.writerow(lista)
# Escribir múltiples filas en el archivo CSV
    escritor_csv.writerows(matriz)
print ("Se creo correctamente el archivo .csv"); 

import csv
with open('nuevo_archivo.csv', 'r', newline='', encoding='utf-8') as archivo_csv:
    lector_csv = csv.reader (archivo_csv);
    for x in lector_csv:
        print (x) """
import csv
with open('nuevo_archivo.csv', 'r') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv);
#Recorremos cada fila con un for
    for fila in lector_csv:
        nombre=fila['NOMBRE'];
        edad=int(fila['EDAD']);
        comuna=fila['COMUNA'];
        if edad>=18:
            rango="Es mayor de edad";
        else:
            rango="Es menor de edad";
        print (f"{nombre} tiene {edad} años y {rango}")