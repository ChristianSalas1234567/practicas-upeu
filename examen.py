#ejercicio 1.1
def notaDeFundamentosDeProgramacionCSY():
  print("notas de fundamentos de programacion")
  #datos de entrada
  Nota1=float(input("nota de unidad 1:"))
  Nota2=float(input("nota de unidad 2:"))
  Nota3=float(input("nota de unidad 3:"))
  Nota4=float(input("nota de unidad 4:"))
  #proceso
  unidad1=(Nota1*0.20)
  unidad2=(Nota2*0.15)
  unidad3=(Nota3*0.15)
  unidad4=(Nota4*0.50)
  #DATOS DE SALIDA
  notaF=(unidad1+unidad2+unidad3+unidad4)
  print(f"tu nota final es:{notaF}")
#notaDeFundamentosDeProgramacionCSY()



#ejercicio 1.2
def bonoporpuntuacionCSY():
  print("bono por su esfuerzo")
  #datos de entrada
  puntos=float(input("ponga la cantidad de puntos que obtuvo: "))
  salario=int(input("cantidad de salario: "))
  #proceso
  if puntos:
    if puntos==50 or puntos<101:
      print(f"tienes un bono de %10 , un salrario minimo de ${salario*0.10}")
    if puntos==101 or puntos<151:
      print(f"tienes un bono de %40 , un salrario minimo de ${salario*0.40}")
    if puntos>=151:
      print(f"tienes un bono de %70, un salrario minimo de ${salario*0.70}")
#bonoporpuntuacionCSY()


#ejercicio 1.3
def VacunasParaCovidCSY():
  print("vacunas covid-19")
  #datos de entrada
  edad=int(input("indicar la edad que tienes:  "))
  #proceso
  if edad:
    if edad<16:
      print("recibiras la vacuna tipo A")
    if edad==16 or edad<=69:
      print("si eres de genero masculino recibiras la vacuna tipo A si eres de genero femenino recibiras la vacuna tipo B")
    if edad==70 or edad>70:
      print("recibiras la vacuna tipo C")
#VacunasParaCovidCSY()


#ejercicio 1.4
def OperacioneDeAritmeticaCSY():
  print("operaciones aritmeticas")
  #datos de entrada
  a=int(input("escriba el valor numero 1:  "))
  b=int(input("escriba el valor numero 2:  "))
  operacion=int(input("escriba el valor de la operacion:  (+)=1,  (-)=2, (/)=3,  (*)=4,  (^)=5 :  "))
  #proceso
  if operacion:
    if operacion==1:
      print(f"el resultado de la operacion es: {a+b}")
    if operacion==2:
      print(f"el resultado de la operacion es: {a-b}")
    if operacion==3:
      print(f"el resultado de la operacion es: {a/b}")
    if operacion==4:
      print(f"el resultado de la operacion es: {a*b}")
    if operacion==5:
      print(f"el resultado de la operacion es: {a**b}")
#OperacioneDeAritmeticaCSY()



#ejercicio 1.5
def EstructuracondicionalCSY():
  #datos de entrada
  ejercicio=int(input("numero de ejercicio:  "))
  #proceso
  if ejercicio:
    if ejercicio==1:
      #ejercicio 1.1
      def notaDeFundamentosDeProgramacionCSY():
        print("notas de fundamentos de programacion")
        #datos de entrada
        Nota1=float(input("nota de unidad 1:"))
        Nota2=float(input("nota de unidad 2:"))
        Nota3=float(input("nota de unidad 3:"))
        Nota4=float(input("nota de unidad 4:"))
        #proceso
        unidad1=(Nota1*0.20)
        unidad2=(Nota2*0.15)
        unidad3=(Nota3*0.15)
        unidad4=(Nota4*0.50)
        #DATOS DE SALIDA
        notaF=(unidad1+unidad2+unidad3+unidad4)
        print(f"tu nota final es:{notaF}")
      notaDeFundamentosDeProgramacionCSY()
    if ejercicio==2:
      #ejercicio 1.2
      def bonoporpuntuacion():
        print("bono por su esfuerzo")
        #datos de entrada
        puntos=float(input("ponga la cantidad de puntos que obtuvo: "))
        salario=int(input("cantidad de salario: "))
        #proceso
        if puntos:
          if puntos==50 or puntos<101:
            print(f"tienes un bono de %10 , un salrario minimo de ${salario*0.10}")
          if puntos==101 or puntos<151:
            print(f"tienes un bono de %40 , un salrario minimo de ${salario*0.40}")
          if puntos>=151:
            print(f"tienes un bono de %70, un salrario minimo de ${salario*0.70}")
      bonoporpuntuacion()
    if ejercicio==3:
      #ejercicio 1.3
      def VacunasParaCovid():
        print("vacunas covid-19")
        #datos de entrada
        edad=int(input("indicar la edad que tienes:  "))
        #proceso
        if edad:
          if edad<16:
            print("recibiras la vacuna tipo A")
          if edad==16 or edad<=69:
            print("si eres de genero masculino recibiras la vacuna tipo A si eres de genero femenino recibiras la vacuna tipo B")
          if edad==70 or edad>70:
            print("recibiras la vacuna tipo C")
      VacunasParaCovid()
    if ejercicio==4:
      #ejercicio 1.4
      def OperacioneDeAritmetica():
        print("operaciones aritmeticas")
        #datos de entrada
        a=int(input("escriba el valor numero 1:  "))
        b=int(input("escriba el valor numero 2:  "))
        operacion=int(input("escriba el valor de la operacion:  (+)=1,  (-)=2, (/)=3,  (*)=4,  (^)=5  "))
        #proceso
        if operacion:
          if operacion==1:
            print(f"el resultado de la operacion es: {a+b}")
          if operacion==2:
            print(f"el resultado de la operacion es: {a-b}")
          if operacion==3:
            print(f"el resultado de la operacion es: {a/b}")
          if operacion==4:
            print(f"el resultado de la operacion es: {a*b}")
          if operacion==5:
            print(f"el resultado de la operacion es: {a**b}")
      OperacioneDeAritmetica()
#EstructuracondicionalCSY()

