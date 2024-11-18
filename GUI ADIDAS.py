from wsgiref.validate import validator
import pandas as pd
import matplotlib.pyplot as ply
import seaborn as sns  
import numpy as np




#dataset = pd.read_csv('G:/Mi unidad/UAO/INGENIERÍA DE DATOS E I.A/SEMESTRE 2/PROGRAMACIÓN/dset.csv', header = None)
dataset= pd.read_excel('G:/Mi unidad/UAO/INGENIERÍA DE DATOS E I.A/SEMESTRE 2/PROGRAMACIÓN/datasetadidas.xlsx')  

print(dataset)  # muestra el dataset y columnas y filas

print(dataset.shape)  # muestra columnas y filas

dataset.head()  #muestra los 5 primeros registros


dataset.info() #cuales son variable categoricas y las numericas
                # int= numericas  #object= categoricas
                
                


# 2 LIMPIEZA

'''
datos faltantes
datos irrelevantes
registros repretidos: filas con la misma informacion
valores extremos aveces: columnas con datos no reales, pueden haberse digitado mal
errores de estructuras en variables categoricas
'''


#datos incompletos: eliminar los datos faltantes

dataset.dropna(inplace=True) # elimina la fila completa con los datos faltantes y el inplace lo reescribe
dataset.info() # verificar la misma cantidad de filas


#columnas irrelevantes: eliminarlas 

del dataset['Retailer ID']
dataset.info()


#cambiar nombre de columnas

dataset=dataset.rename(columns= {'Retailer':'Minorista', 'Invoice Date':'Fecha de facturación', 'Region':'Región', 'State': 'Estado', 'City':'Ciudad', 'Product':'Producto', 'Price per Unit':'Precio por Unidad', 'Units Sold':'Unidades Vendidas', 'Total Sales':'Ventas Totales', 'Operating Profit':'Beneficio operativo', 'Operating Margin':'Margen operativo', 'Sales Method':'Método de venta'})
print(dataset)




#3. Interfaz Grafica de Usuario

import tkinter
from tkinter import*
from PIL import ImageTk, Image



window= tkinter.Tk()

window.title('Adidas US Sales Dataset')

window.geometry('1600x850')



# imagen de adidas

imagen= ImageTk.PhotoImage(Image.open('C:/Users/braya/OneDrive/Imágenes/adidas.jpg').resize((1600,780)))
labelimg= tkinter.Label(image=imagen)
labelimg.pack()




#interfaz ventana 1



label1= Label(window, text= 'Escribe tu nombre de usuario', width=30, bg='Snow')
label1.place(x=600, y=545)
label1.configure(font=("Courier", 14,"bold"))

entry1= Entry(window, width=25, bg= 'Gainsboro')
entry1.place(x=670, y=585, height=30, width=200)
entry1.configure(font=(15))


label2= Label(window, text= 'Escribe tu contraseña', width=30, bg='Snow')
label2.place(x=600, y=625)
label2.configure(font=("Courier", 14,"bold"))

entry2= Entry(window, width=25, show='*', bg= 'Gainsboro')
entry2.place(x=670, y=665, height=30, width=200)
entry2.configure(font=(15))


#ventana 2

from tkinter import ttk
from tkinter import messagebox





def validar():
    
    usuario= str(entry1.get())
    contraseña = int(entry2.get())
    if usuario == 'user1234' and contraseña == 1234:
                window2= Toplevel()
                window2.title('Ventana secundaria')
                window2.geometry('1600x850')
                button3= ttk.Button(window2, text='Salir', command=window2.destroy)  
                button3.place(x=720, y=740, height=30, width=100)
                window2.focus()
                window2.grab_set()
                
                
                button_line = ttk.Button(window2, text='Gráfico de barras',command=bar_plot)  #boton de grafico de barras
                button_line.place(x=705, y=50, height=80, width=130)
                
                
                button_box = ttk.Button(window2, text='Gráfico circular', command=torta)  #boton de grafico de pie
                button_box.place(x=705, y=150, height=80, width=130)
                
                
                
                button_histogram = ttk.Button(window2, text='Histograma', command=histogram)  #Histograma
                button_histogram.place(x=705, y=250, height=80, width=130)
                
                
                
                button_dispercion = ttk.Button(window2, text='Diagrama de disperción', command= scatter_plot) #Diagrama de disperción
                button_dispercion.place(x=705, y=350, height=80, width=130)
                
                
                
                
                button_3d = ttk.Button(window2, text='Grafico 3D',command= tresd) #Grafico 3D
                button_3d.place(x=705, y=450, height=80, width=130)
                
                
                
                
                button_analis = ttk.Button(window2, text='Data Analysis',command= analisis) #Analisis
                button_analis.place(x=705, y=550, height=80, width=130)
                
                
                
                button_analis = ttk.Button(window2, text='Correlacion',command= correlacion) #Correlacion
                button_analis.place(x=705, y=650, height=80, width=130)
                


                

                
    else:
        messagebox.showerror(message='Datos incorrectos', title='Error') 


#Graficas 

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import(FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt



#1. Grafico de barras


def bar_plot():
    # Datos de ejemplo
    x = (dataset["Producto"])
    y = (dataset["Unidades Vendidas"])
    
    # Crear el gráfico de barras
    plt.bar(x, y, color='blue')
    
    # Título y etiquetas de los ejes
    plt.title('Unidades Vendidas x Tipo de producto')
    plt.xlabel('Tipo de producto')
    plt.ylabel('Cantidad de unidades vendidas')
    
    # Mostrar el gráfico
    plt.show()


#2. Grafico de torta

    
def torta():
    ventas_por_region = dataset['Región'].value_counts()
    print (ventas_por_region)
    # Crear el gráfico de torta
    plt.figure(figsize=(8, 8))
    plt.pie(ventas_por_region, labels=ventas_por_region.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribución de ventas por regiones de USA')
    plt.show()



#3. Histograma

def histogram():
    plt.hist(dataset['Fecha de facturación'], bins=200, color='blue')
    plt.title('Reporte fechas de facturación')
    plt.xlabel('Fecha de facturación')
    plt.ylabel('Cantidad de reportes')
    plt.show()



#4. Diagrama de dispercion


def scatter_plot ():
    plt.figure(figsize=(8, 6))
    plt.scatter(dataset['Precio por Unidad'], dataset['Unidades Vendidas'], color='blue')
    plt.title('Gráfico de dispersión: Precio por unidad vs Unidades vendidas')
    plt.xlabel('Precio por unidad')
    plt.ylabel('Unidades vendidas')
    plt.show()



#5. Grafico 3d

import plotly.express as px

def tresd():

    fig = px.scatter_3d(dataset, x='Margen operativo', y='Beneficio operativo', z='Ventas Totales')
    fig.show()
    
    


# 6. Data Analisis

import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk



def analisis():
    df = dataset.copy()
    del df['Fecha de facturación']
    
    window3 = tk.Toplevel()
    window3.title('Ventana análisis')
    window3.geometry('800x600')
    window3.focus()
    window3.grab_set()
    descripcion_df = df.describe()

    estilo = ttk.Style()
    estilo.configure('Treeview', font=('Arial', 12))  # Ajusta aquí el tamaño y la fuente de la letra

    tabla = ttk.Treeview(window3, style='Treeview')
    tabla["columns"] = list(descripcion_df.columns)
    tabla.heading("#0", text="Estadística")

    for col in descripcion_df.columns:
        tabla.heading(col, text=col)
        tabla.column(col, width=200)
    for i, (index, row) in enumerate(descripcion_df.iterrows()):
        tabla.insert("", i, text=index, values=list(round(row,2)))
    tabla.pack()



#7. Grafico de correlacion

def correlacion():
    import matplotlib.pyplot as plt
    import pandas as pd

    numeric_columns = dataset.select_dtypes(include=['float64', 'int64'])
    # Crear una matriz de correlación
    correlation_matrix = numeric_columns.corr()

    # Crear el gráfico de correlación
    plt.figure(figsize=(10, 8))
    plt.matshow(correlation_matrix, cmap='coolwarm', fignum=1)
    plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation='horizontal')
    plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
    plt.colorbar(label='Correlation Coefficient')
    plt.title('Correlation Matrix')
    plt.show()











#botones ventana 1


button1= Button(window, text='Continuar', height=30, width=15, activebackground='Darkblue', bg='Snow', command= validar)
button1.place(x=660, y=720, height=40, width=110)
button1.configure(font=("Arial", 15, "bold"))


button2= Button(window, text='Salir', command=window.quit, activebackground='Darkblue', bg='Snow')
button2.place(x=775, y=720, height=40, width=110)
button2.configure(font=("Arial", 15, "bold"))





window.mainloop()




















