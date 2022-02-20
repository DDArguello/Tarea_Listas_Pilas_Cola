class Lista:
  def __init__(self,datos=['12','15','48','78']):
    self.lista=datos

  def empty(self):
      return len(self.lista)==0
  
  def insertar(self,dato):
    self.lista.append(dato)
  
  def obtener(self):
      if self.empty():
        return "lista Vacia"
      else:
       return self.lista.pop()
  
  def elimElem(self,pos):
    if pos in range(0,len(self.lista)):
        elem=self.lista[pos]
        self.lista=self.lista[0:pos]+self.lista[pos+1:]
        return f"Se elimino el elemento {elem}"
    else: return f"posicion {pos} no existe en la lista"

  def inserElem(self,pos,dato):
    self.lista.insert(pos,dato)
    return self.lista

  def buscar(self,buscado):
      self.buscado=str(buscado)
      if self.empty():
        return "Lista Vacia"
      else:
        for i in range(len(self.lista)):
          if self.lista[i]==self.buscado:
            return f"El elemento {self.buscado} se encuentra en la posicion {i} de la lista"
        return f"No existe el elemento {self.buscado} en la lista"

  def mostrar(self):
    if self.empty():
      print("lista Vacia")
    else:
          print(self.lista)
      # for tope in self.lista:
      #   print(f"[{tope}]")
