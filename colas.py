class Cola:
    #MOdificar todo !!!!!!
    def __init__(self,tam):
      self.lista=[]
      self.tope=0
      self.size=tam
    
    def empty(self):
      return self.tope==0
    
    def push(self,dato):
      if self.tope<self.size:
        self.lista+=[dato]
        self.tope+=1
      else: print("La lista esta llena")

    def pop(self):
      if self.empty():
        return -1
      else:
        top=self.lista[0]
        self.tope-=1
        self.lista.remove(top)
        return top
      
    def long(self):
      return self.tope
    
    def show(self):
      if self.empty():
        print("lista Vacia")
      else:
        for tope in self.lista:
          print(f"[{tope}]")
    
    def buscar(self,buscado):
      self.buscado=str(buscado)
      if self.empty():
        return "Lista Vacia"
      else:
        for i in range(self.tope):
          if self.lista[i]==self.buscado:
            return f"El elemento {self.buscado} se encuentra en la posicion {i} de la lista"
          else: None
                
      #return "retorna la posicion del valor buscado"