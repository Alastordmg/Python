import pandas as pd

df = pd.read_excel('tabla2.xlsx')
print(df.columns)
values = df['Id'].values
print(values)
df.describe()

#mostrar tabla
columnas = ['Id', 'Nombre', 'Nivel_De_Poder']
df_seleccionados = df[columnas]
print(df_seleccionados)

df['Incremento_De_Poder'] = df.Nivel_De_Poder.apply(lambda x: \
                        	x*4 if x > 8000 else x*2)

df.to_excel('resultado.xlsx', sheet_name='Hoja1')                            

overpower = df[df.Incremento_De_Poder > 40000]   
with open('max.txt', 'w') as gen_file:
     gen_file.write('')   

for i in overpower.index:  
    with open("max.txt", "a") as max_power:
     max_power.write('Se detecto un alto nivel de poder en la fila : ' + str(overpower["Id"][i]) +'\n')


# Replace missing values to None
#auto['city-mpg'] = auto['city-mpg'].replace(['missing'], np.nan)
#print(auto['city-mpg'].unique())     

# Change data type
#auto['city-mpg'] = auto['city-mpg'].astype('float')
                          
# Change the data type of `Rating` to category
#clothes['Rating'] = pd.Categorical(clothes['Rating'], \ 
# ['very unsatisfied', 'unsatisfied', 'neutral', 'satisfied', 'very satisfied'], ordered = True)                          

#Cat codes asigna valor numerico a cada categoria
#median_index = np.median(df['education'].cat.codes)
#print(median_index) # Output: 9

#For ordinal categorical data
#nintieth_perc_ind = np.percentile(df['education'].cat.codes, 90)
#nintieth_perc_cat = correct_order[int(nintieth_perc_ind)]
#print(nintieth_perc_cat): #output: Bachelors

#calcular proporciones de valores de columna, sin incluir missing
#health_proportions = nyc_trees['health'].value_counts(normalize = True)
#calcular proporciones de valores de columna, incluyendo missing
#health_proportions_2 = nyc_trees['health'].value_counts(normalize = True, dropna = False)

#Then, we can use the sum or mean to calculate a frequency or proportion of Trues in the data.
#change the value for the one u want to calculate
#(df.workclass == 'Local-gov').sum()  #output: 2093
#(df.workclass == 'Local-gov').mean() #output: 0.064