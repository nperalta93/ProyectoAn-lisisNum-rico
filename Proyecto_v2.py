import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
from sympy import *
import math
import matplotlib.pyplot as plt
import numpy as np

class AppIntegracion(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.title_font = tkfont.Font(family='Helvetica', size=18)
		container=tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		
		self.frames={}
		for F in (Inicio, Simpson, Trapecio, Romberg, Grafica):
			pagina=F.__name__
			frame = F(parent=container, controller=self)
			self.frames[pagina] = frame 	
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame("Inicio")

	def show_frame(self, pagina):
		frame= self.frames[pagina]
		frame.tkraise()

class Inicio(tk.Frame):
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		self.controller=controller
		label=tk.Label(self, text="Aplicación de métodos de integración numérica", font=controller.title_font)
		label.pack(side="top", fill="x", pady=30)
		
		x=Symbol('x')
		x5=tk.StringVar(self)
		txtX5=Entry(self, textvariable=x5, width=15).pack()
		
		def work():
			"""
			for i	 in range (1, 5):		
				p = np.poly1d([i, i, i, i, i])
			return p
			"""
			def please():
				helli=x5.get()
				return helli
			yellow=please()
			print (yellow)
			
		buttonP=tk.Button(self, text="Capturar", command=lambda:work())
		buttonP.pack()
		buttonRes=tk.Button(self, text="Resolver", command=lambda:work())
		buttonRes.pack()
		buttonS=tk.Button(self, text="Regla de Simpson", command=lambda: controller.show_frame("Simpson"))
		buttonT= tk.Button(self, text="Regla del trapecio", command=lambda: controller.show_frame("Trapecio"))
		buttonR= tk.Button(self, text="Método de Romberg", command=lambda: controller.show_frame("Romberg"))
		buttonG= tk.Button(self, text="Gráfica comparativa", command=lambda: controller.show_frame("Grafica"))
		buttonS.pack()
		buttonT.pack()
		buttonR.pack()
		buttonG.pack()

class Simpson(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		self.controller=controller
		label=tk.Label(self, text="Regla de Simpson", font=controller.title_font)
		label.pack(side="top", fill="x", pady=10)
		
		def mostrar():
			def f(x):
			  return sin(x)

			def simpson_rule(a,b):
			  #Approximation by Simpson's rule
			  c=(a+b)/2.0
			  h=abs(b-a)/2.0
			  return h*(f(a)+4.0*f(c)+f(b))/3.0

			resultado=simpson_rule(0,1)
			lblSim=Label(self, text="Resultado: " +str(resultado),font=("agency FB",14)).pack()
			S=Scrollbar(self)
			T=Text(self, height=4, width=50)
			S.pack(side=RIGHT, fill=Y)
			T.pack()
			S.config(command=T.yview)
			T.config(yscrollcommand=S.set)
			quote = """Este  método  consiste  en  la  aproximación del  cálculo  del  área  plana  bajo  una  curva  utilizando trapecios curvilíneos a partir una interpolación con una función cuadrática"""
			T.insert(END, quote)

			return resultado
		
		buttonSh=tk.Button(self, text="Mostrar resultados", command=lambda: mostrar())
		buttonSh.pack()		
		buttonRet=tk.Button(self, text="Regresar a la página principal", command=lambda: controller.show_frame("Inicio"))
		buttonRet.pack()

class Trapecio(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		self.controller=controller
		label=tk.Label(self, text="Regla del Trapecio", font=controller.title_font)
		label.pack(side="top", fill="x", pady=10)
		
		def mostrar():

			def f(x):
			  return sin(x)

			def trapecio (a,b,n):
				h=(b-a)/n
				S=0.5*(f(a)+f(b))
				for i in range (1, n):
					S += f(a+i*h)
				Integral = h*S
				return Integral
			resultado=trapecio(0,1,100)
			lblSim=Label(self, text="Resultado: " +str(resultado),font=("agency FB",14)).pack()
			
			S=Scrollbar(self)
			T=Text(self, height=4, width=50)
			S.pack(side=RIGHT, fill=Y)
			T.pack()
			S.config(command=T.yview)
			T.config(yscrollcommand=S.set)
			quote = """En análisis numérico la regla del trapecio es un método de integración, es decir, un método para calcular aproximadamente el valor de una integral definida. La regla se basa en aproximar el valor de la integral de f (x) por el de la función lineal, que pasa a través de los puntos (a, f(a)) y (b, f(b)). La integral de ésta es igual al área del trapecio bajo la gráfica de la función lineal."""
			T.insert(END, quote)
	
		buttonSh=tk.Button(self, text="Mostrar resultados", command=lambda: mostrar())
		buttonSh.pack()		
		buttonRet=tk.Button(self, text="Regresar a la página principal", command=lambda: controller.show_frame("Inicio"))
		buttonRet.pack()

class Romberg(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		self.controller=controller
		label=tk.Label(self, text="Método de Romberg", font=controller.title_font)
		label.pack(side="top", fill="x", pady=10)

		def mostrar():
		
			def f(x):
			  return sin(x)

			def trapezcomp(f, a, b, n):
  	  # Initialization
					h = (b - a) / n
					x = a 
  	  # Composite rule
					In = f(a)
					for k in range(1, n):
						x  = x + h
						In += 2*f(x)
	
					return (In + f(b))*h*0.5
 	
			def romberg(f, a, b, p):
				I = np.zeros((p, p))
				for k in range(0, p):
  	     # Composite trapezoidal rule for 2^k panels
					I[k, 0] = trapezcomp(f, a, b, 2**k)
  	     # Romberg recursive formula
					for j in range(0, k):
						I[k, j+1] = (4**(j+1) * I[k, j] - I[k-1, j]) / (4**(j+1) - 1)
 	
					print(I[k,0:k+1])   # display intermediate results
				return I
			
			p_rows = 4
			I = romberg(f, 0, np.pi/2, p_rows)
			solution = I[p_rows-1, p_rows-1]
			lblSim=Label(self, text="Resultado: " +str(solution),font=("agency FB",14)).pack()		
			S=Scrollbar(self)
			T=Text(self, height=10, width=50)
			S.pack(side=RIGHT, fill=Y)
			T.pack()
			S.config(command=T.yview)
			T.config(yscrollcommand=S.set)
			quote = """En análisis numérico, el Método de Romberg genera una matriz triangular cuyos elementos son estimaciones numéricas de la integral definida. Esto, usando la extrapolación de Richardson de forma reiterada en la regla del trapecio. El método de Romberg evalúa el integrando en puntos equiespaciados del intervalo de integración estudiado. Para que este método funcione, el integrando debe ser suficientemente derivable en el intervalo, aunque se obtienen resultados bastante buenos incluso para integrandos poco derivables. Aunque es posible evaluar el integrando en puntos no equiespaciados, en ese caso otros métodos como la cuadratura gaussiana o la cuadratura de Clenshaw–Curtis son más adecuados."""
			T.insert(END, quote)

		buttonSh=tk.Button(self, text="Mostrar resultados", command=lambda: mostrar())
		buttonSh.pack()		
		buttonRet=tk.Button(self, text="Regresar a la página principal", command=lambda: controller.show_frame("Inicio"))
		buttonRet.pack()

class Grafica(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		self.controller=controller
		label=tk.Label(self, text="Gráfica comparativa", font=controller.title_font)
		label.pack(side="top", fill="x", pady=10)
		def Grafica():		
			def f(x):
  			#La función a integrar
				return sin(x)

			def simpson(a,b):
			  c=(a+b)/2.0
			  h=abs(b-a)/2.0
			  return h*(f(a)+4.0*f(c)+f(b))/3.0
	
			def trapecio (a,b,n):
				h=(b-a)/n
				S=0.5*(f(a)+f(b))
				for i in range (1, n):
					S += f(a+i*h)
				Integral = h*S
				return Integral

			def trapezcomp(f, a, b, n):
    # Initialization
				h = (b - a) / n
				x = a 
    # Composite rule
				In = f(a)
				for k in range(1, n):
					x  = x + h
					In += 2*f(x)

				return (In + f(b))*h*0.5
 
			def romberg(f, a, b, p):
				I = np.zeros((p, p))
				for k in range(0, p):
        # Composite trapezoidal rule for 2^k panels
					I[k, 0] = trapezcomp(f, a, b, 2**k)
        # Romberg recursive formula
					for j in range(0, k):
						I[k, j+1] = (4**(j+1) * I[k, j] - I[k-1, j]) / (4**(j+1) - 1)
 
					print(I[k,0:k+1])   # display intermediate results
 
				return I

			p_rows = 4
			I = romberg(f, 0, np.pi/2, p_rows)
			solution = I[p_rows-1, p_rows-1]
			print(solution)
			print (simpson(0,1))
			print (trapecio(0,(2),100))
			simpson=(simpson(0,1))
			trapecio=(trapecio(0,(pi/2),100))
			romberg=solution
	
			nombres = []
			nombres.append("Simpson")
			nombres.append("Trapecio")
			nombres.append("Romberg")
			ss = []
			ss.append(simpson)
			ss.append(trapecio)
			ss.append(romberg)
			#plt.axes((0.1, ))  # Definimos la posición de los ejes
			plt.bar(np.arange(3), ss)  # Dibujamos el gráfico de barras
			plt.ylim(0, 2)  # Limitamos los valores del eje y al range definido [450, 550]
			plt.title('Métodos de integración')  # Colocamos el título
			plt.xticks(np.arange(3), nombres, rotation = 45)  # Colocamos las etiquetas del eje x, en este caso, las fechas
			plt.show()

		buttonSh=tk.Button(self, text="Mostrar resultados", command=lambda: Grafica())
		buttonSh.pack()
		buttonRet=tk.Button(self, text="Regresar a la página principal", command=lambda: controller.show_frame("Inicio"))
		buttonRet.pack()
		
if __name__ == "__main__":
	app=AppIntegracion()
	app.title("Integración numérica")
	app.mainloop() 
	
