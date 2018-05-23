from tkinter import *

import math
import matplotlib.pyplot as plt
import numpy as np

def limInicial():
	lblSaludar=Label(ventana,text="limite inicial-> " + entradaU.get(), font=("agency FB", 14)).place(x=290,y=10)

def limFinal():
	lblDespide=Label(ventana, text="limite final-> "+entradaN.get(),font=("agency FB",14)).place(x=290,y=45)

def poli():
	lblDespide2=Label(ventana, text="funcion trigonometrica-> "+entradaP.get(),font=("agency FB",14)).place(x=400,y=80)

def limInicial2():
	lblSaludar2=Label(ventana,text="limite inicial-> " + entradaTra.get(), font=("agency FB", 14)).place(x=290,y=210)

def limFinal2():
	lblDespide3=Label(ventana, text="limite final-> "+entradaTra2.get(),font=("agency FB",14)).place(x=290,y=240)

def n2():
	lblDespide4=Label(ventana, text="numero puntos-> "+entradaTra3.get(),font=("agency FB",14)).place(x=400,y=270)

def poli2():
	lblDespide5=Label(ventana, text="funcion trigonometrica-> "+entradaT.get(),font=("agency FB",14)).place(x=400,y=300)

def simpson():
	def f(x):
	  #function to integrate
	  trig=entradaP.get()
	  #po=math.polinomio
	  x = getattr(math, trig)(x)
	  return x


#3x^2-4x+2


	def simpson_rule(a,b):
	  #Approximation by Simpson's rule
	  c=(a+b)/2.0
	  h=abs(b-a)/2.0
	  return h*(f(a)+4.0*f(c)+f(b))/3.0

	# Calculates integral of f(x) from 0 to 1
	ini=int(entradaU.get())
	fin=int(entradaN.get())

	resultado=simpson_rule(ini,fin)
	
	lblPol=Label(ventana, text="Resultado--> "+str(resultado),font=("agency FB",14)).place(x=10,y=170)
	return resultado

def trapecios():
	def f(x):
	  #function to integrate
	  trig2=entradaT.get()
	  #po=math.polinomio
	  x = getattr(math, trig2)(x)
	  return x
	def trap (a,b,n):
	  h=(b-a)/n
	  S=0.5*(f(a)+f(b))
	  for i in range (1, n):
	    S += f(a+i*h)
	  Integral = h*S
	  return Integral
	a=int(entradaTra.get())
	b=int(entradaTra2.get())
	c=int(entradaTra3.get())

	resultado2=trap(a,b,c)

	lblPol2=Label(ventana, text="Resultado--> "+str(resultado2),font=("agency FB",14)).place(x=10,y=380)
	return resultado2

def graficas():
	nombres = []
	nombres.append("Simpson")
	nombres.append("Trapecio")
	ss = []
	ss.append(simpson())
	ss.append(trapecios())
	#plt.axes((0.1, ))  # Definimos la posición de los ejes
	plt.bar(np.arange(2), ss)  # Dibujamos el gráfico de barras
	plt.ylim(0, 2)  # Limitamos los valores del eje y al range definido [450, 550]
	plt.title('Métodos de integración')  # Colocamos el título
	plt.xticks(np.arange(2), nombres, rotation = 45)  # Colocamos las etiquetas del eje x, en este caso, las fechas
	plt.show()

ventana=Tk()
ventana.geometry("800x450+100+100")
ventana.title("Proyecto Analisis Numerico")

lblUsuario=Label(text="Limite inicio:", font=("Agency FB", 14)).place(x=10, y=10)
entradaU=StringVar()
txtUsuario=Entry(ventana,textvariable=entradaU,width=5).place(x=150,y=15)
lblNombre=Label(text="Limite fin:", font=("Agency FB", 14)).place(x=10,y=50)
entradaN=StringVar()
txtNombre=Entry(ventana,textvariable=entradaN,width=5).place(x=150,y=55)
lblNombre2=Label(text="Funcion trigonometrica:", font=("Agency FB", 14)).place(x=10,y=90)
entradaP=StringVar()
txtNombre2=Entry(ventana,textvariable=entradaP,width=5).place(x=250,y=95)
btnSaludar=Button(ventana,text="Validar", command=limInicial,font=("Agency FB", 14), width=5).place(x=200,y=10)
btnDespedir=Button(ventana,text="Validar",command=limFinal, font=("Agency FB", 14), width=5).place(x=200, y=45)
btnPoli=Button(ventana,text="Validar",command=poli, font=("Agency FB", 14), width=5).place(x=310, y=80)
btnSimpson=Button(ventana,text="Simpson",command=simpson, font=("Agency FB", 14), width=5).place(x=200, y=130)

lblTra=Label(text="Limite inicio:", font=("Agency FB", 14)).place(x=10, y=210)
entradaTra=StringVar()
txtTra=Entry(ventana,textvariable=entradaTra,width=5).place(x=150,y=215)
lblTra2=Label(text="Limite fin:", font=("Agency FB", 14)).place(x=10,y=240)
entradaTra2=StringVar()
txtTra2=Entry(ventana,textvariable=entradaTra2,width=5).place(x=150,y=245)
lblTra3=Label(text="numero puntos:", font=("Agency FB", 14)).place(x=10,y=270)
entradaTra3=StringVar()
txtTra3=Entry(ventana,textvariable=entradaTra3,width=5).place(x=180,y=275)
lblt=Label(text="Funcion trigonometrica:", font=("Agency FB", 14)).place(x=10,y=300)
entradaT=StringVar()
txtt=Entry(ventana,textvariable=entradaT,width=5).place(x=250,y=305)
btnSaludar=Button(ventana,text="Validar", command=limInicial2,font=("Agency FB", 14), width=5).place(x=200,y=210)
btnDespedir=Button(ventana,text="Validar",command=limFinal2, font=("Agency FB", 14), width=5).place(x=200, y=240)
btnPoli=Button(ventana,text="Validar",command=n2, font=("Agency FB", 14), width=5).place(x=310, y=270)
btnPoli=Button(ventana,text="Validar",command=poli2, font=("Agency FB", 14), width=5).place(x=310, y=300)
btnSimpson=Button(ventana,text="Trapecios",command=trapecios, font=("Agency FB", 14), width=6).place(x=230, y=340)
btnGrafica=Button(ventana, text="Gráfica comparativa", command=graficas, font=("Agency FB", 14), width=20).place(x=230, y=400)

ventana.mainloop()
