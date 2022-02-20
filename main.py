from socket import timeout
from Title import Titulo
from listas import Lista
from pilas import Stack
from colas import Cola
import os
#Inico
titulo = Titulo()
lista1=Lista()
lista = ["1) Listas","2) Pilas","3) Colas","4) Salir"]
opcion=""
while opcion != "4":
  os.system("cls")
  opcion = titulo.menu(lista,"MENU PRINCIPAL")
  if opcion == "1":
    opc1=""
    while opc1 != "7":
      os.system("cls")
      opc1 = titulo.menu(["1) Push","2) Pop","3) Show","4) Eliminar","5) Insertar","6) Buscar","7) Salir"],"LISTAS")
      os.system("cls")
      if opc1 == "1":
          print("*"*20,"PUSH","*"*20)
          lista1.insertar(input("Ingrese elemento: "))
          lista1.mostrar()
          input("Presione una tecla para continuar...")  
      elif opc1 == "2":
        print("*"*20,"POP","*"*20)
        lista1.mostrar()
        print(lista1.obtener())
        input("Presione una tecla para continuar...")  
      elif opc1=='3':
          print("*"*20,"SHOW","*"*20)
          lista1.mostrar()
          input("Presione una tecla para continuar...")  
      elif opc1=='4':
          print("*"*20,"ELIMINAR","*"*20)
          lista1.mostrar()
          print(lista1.elimElem(int(input("Ingrese posicion del elemento a eliminar: "))))
          lista1.mostrar()
          input("Presione una tecla para continuar...")  
      elif opc1=='5':
          print("*"*20,"INSERTAR","*"*20)
          lista1.mostrar()
          print(lista1.inserElem(int(input("Ingrese posicion en donde desea insertar el nuevo elemento:  ")),input("Ingrese el elemento a insertar:  ")))
          input("Presione una tecla para continuar...")
      elif opc1=='6':
          print("*"*20,"BUSCAR","*"*20)
          print(lista1.buscar(input("Ingrese el elemento a buscar: ")))
          input("Presione una tecla para continuar...")  
  elif opcion == "2":
    opc1=""
    pila=Stack(5)
    while opc1 != "6":
      os.system("cls")
      opc1 = titulo.menu(["1) Push","2) Pop","3) Show","4) Buscar","5) Longitud","6) Salir"],"PILAS")
      os.system("cls")
      if opc1 == "1":
          print("*"*20,"PUSH","*"*20)
          pila.push(input("Ingrese elemento: "))
          pila.show()
          input("Presione una tecla para continuar...")  
      elif opc1 == "2":
        print("*"*20,"POP","*"*20)
        pila.show()
        print(' ')
        resp=pila.pop()
        if resp==-1:
            print("Lista vacia")
        else: print(resp,'\n'), pila.show()
        input("Presione una tecla para continuar...")  
      elif opc1=='3':
          print("*"*20,"SHOW","*"*20)
          pila.show()
          input("Presione una tecla para continuar...")  
      elif opc1=='4':
          print("*"*20,"BUSCAR","*"*20)
          x=pila.buscar(input("Ingrese el elemento a buscar: "))
          if x==None:
              print("No existe ese elemento en la lista")
          else:
              print(x)
          input("Presione una tecla para continuar...") 
      elif opc1=='5':
          print("*"*20,"Longitud","*"*20)
          lon=pila.long()
          print(f"La lista tiene una longitud de {lon}")
          input("Presione una tecla para continuar...")  
  elif opcion == "3":
    opc1=""
    cola=Cola(5)
    while opc1 != "6":
      os.system("cls")
      opc1 = titulo.menu(["1) Push","2) Pop","3) Show","4) Buscar","5) Longitud","6) Salir"],"COLAS")
      os.system("cls")
      if opc1 == "1":
          print("*"*20,"PUSH","*"*20)
          cola.push(input("Ingrese elemento: "))
          cola.show()
          input("Presione una tecla para continuar...")  
      elif opc1 == "2":
        print("*"*20,"POP","*"*20)
        cola.show()
        print(' ')
        resp=cola.pop()
        if resp==-1:
            print("Lista vacia")
        else: print(resp,'\n'), cola.show()
        input("Presione una tecla para continuar...")  
      elif opc1=='3':
          print("*"*20,"SHOW","*"*20)
          cola.show()
          input("Presione una tecla para continuar...")  
      elif opc1=='4':
          print("*"*20,"BUSCAR","*"*20)
          x=cola.buscar(input("Ingrese el elemento a buscar: "))
          if x==None:
              print("No existe ese elemento en la lista")
          else:
              print(x)
          input("Presione una tecla para continuar...") 
      elif opc1=='5':
          print("*"*20,"Longitud","*"*20)
          lon=cola.long()
          print(f"La lista tiene una longitud de {lon}")
          input("Presione una tecla para continuar...") 

os.system("cls")        
print('*'*20,"Gracias por visitarnos",'*'*20)  
