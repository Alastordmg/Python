import pandas as pd
import xlrd 
#pip install xlrd==1.2.0 
archivo = 'resultado.xlsx'
  
wb = xlrd.open_workbook(archivo) 

hoja = wb.sheet_by_index(0) 
print(hoja.nrows) 
print(hoja.ncols) 
print(hoja.cell_value(0, 0))
print('\n')

#Imprimir fila X
hoja = wb.sheet_by_name('Hoja1') 
for i in range(0,hoja.ncols):
    print(hoja.cell_value(0,i))
print('\n')    

#asignar fila a variable en formato lista
hoja = wb.sheet_by_index(0) 
nombres = hoja.row(0)  
print(nombres) 
print('\n')   

#imprimir columna X
hoja = wb.sheet_by_name('Hoja1') 
for i in range(0,hoja.nrows):
    print(hoja.cell_value(i,1))    
print('\n')

filas = []
for fila in range(1,hoja.nrows):
    columnas = []
    for columna in range(0,2):
        columnas.append(hoja.cell_value(fila,columna))
    filas.append(columnas)

df = pd.DataFrame(filas)
columnas = df.iloc[0]
df_seleccionados = df[columnas]
print(df_seleccionados)
df.head()    