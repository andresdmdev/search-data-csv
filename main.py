import csv

# Fuente de la verdad
dataTrusty_csv = './files/ejemplo.csv'
# Fuente para comparar
dataCompare_csv = './files/dataPrueba.csv'
# Resultado de la comparacion
newData_csv = './files/newData.csv'

"""
with open(archivo_csv, encoding="utf8") as archivo:
  lector_csv = csv.reader(archivo)

  for fila in lector_csv:
    print(f"Nombre: {fila[1]}") """

# Archivo de la fuente de la verdad
dataTrusty = open(dataTrusty_csv,encoding="utf8", newline='')
# Archivo donde buscamos los datos a buscar
dataCompare = open(dataCompare_csv,encoding="utf8", newline='')
# Archivo para guardar los datos encontrados
newData = open(newData_csv, 'w', newline='')

# Cambiar los headers de acuerdo al archivo
headers = ['ID','Proveedor','Contacto comercial','Email','Teléfono',' Saldo pendiente','Fecha de última compra','Fecha expiracion']
newObjectData = csv.DictWriter(newData, fieldnames=headers)
newObjectData.writeheader()

# Convertir todos los datos a objetos para comparar
objData = csv.DictReader(dataTrusty)
objCompare = csv.DictReader(dataCompare)

tempObjectData = []

for rowCompare in objCompare:
  for rowTrusty in objData:
    # Buscar en base a los valores y headers necesarios
    if rowCompare['Teléfono'] == rowTrusty['Teléfono']:
      tempObjectData.append(rowTrusty)
      break
  

newObjectData.writerows(tempObjectData)
print(f'Coincidencias encontradas: {len(tempObjectData)}')
print(f'El archivo esta disponible en: {newData_csv}')

dataTrusty.close()
dataCompare.close()
newData.close()