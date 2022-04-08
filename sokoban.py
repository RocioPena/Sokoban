class Sokoban:

  personaje = 0
  espacio = 1
  caja = 2
  pared = 3
  meta = 4
  personaje_meta = 5
  caja_meta = 6
  
  mapa = []
  personaje_fil = 0
  personaje_col = 0

  def __init__(self):
        pass
  
  def leerMapa(self):
    file = open("mapa1.rps","r")
    self.mapa=[
        [3,3,3,3,3,3,3,3,3,3,3,3],
        [3,1,1,1,1,1,1,1,1,1,1,3],
        [3,1,1,1,1,1,1,1,1,1,1,3],
        [3,1,1,1,1,1,5,1,1,1,1,3],
        [3,1,1,1,1,1,2,1,1,1,1,3],
        [3,1,1,1,1,1,1,1,1,1,1,3],
        [3,1,1,1,1,1,1,1,1,1,1,3],
        [3,1,1,1,1,1,1,1,1,1,1,3],
        [3,3,3,3,3,3,3,3,3,3,3,3]
    ]
#esto firve para leer un archivo de texto

  def imprimirMapa(self):
        for fil in self.mapa:  # For each row in map
            print(fil)

  def posicionPersonaje(self):
  
    for fil in range(len(self.mapa)): 
      for col in range(len(self.mapa[fil])): 
          if self.mapa[fil][col] == 0 or self.mapa[fil][col] == 5: #puede iniciar con 0 o con 5
            self.personaje_fil = fil 
            self.personaje_col = col 
         

  def moverDerecha(self):
    print("te moviste a la derecha") 
    #personaje,espacio
    if (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil][self.personaje_col + 1] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil][self.personaje_col + 1] = self.personaje  
            self.personaje_col = self.personaje_col + 1
    #personaje,meta
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil][self.personaje_col + 1] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil][self.personaje_col + 1] = self.personaje_meta  
            self.personaje_col = self.personaje_col + 1
     #personaje,caja,espacio     
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil][self.personaje_col + 1] == self.caja
            and self.mapa[self.personaje_fil][self.personaje_col + 2] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil][self.personaje_col + 1] = self.personaje 
            self.mapa[self.personaje_fil][self.personaje_col + 2] = self.caja
            self.personaje_col = self.personaje_col + 1
     #personaje,caja,meta     
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil][self.personaje_col + 1] == self.caja
            and self.mapa[self.personaje_fil][self.personaje_col + 2] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil][self.personaje_col + 1] = self.personaje 
            self.mapa[self.personaje_fil][self.personaje_col + 2] = self.caja_meta
            self.personaje_col = self.personaje_col + 1    
     #personaje,caja_meta,espacio     
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil][self.personaje_col + 1] == self.caja_meta
            and self.mapa[self.personaje_fil][self.personaje_col + 2] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil][self.personaje_col + 1] = self.personaje_meta 
            self.mapa[self.personaje_fil][self.personaje_col + 2] = self.caja
            self.personaje_col = self.personaje_col + 1 
     #personaje,caja_meta,meta    
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil][self.personaje_col + 1] == self.caja_meta
            and self.mapa[self.personaje_fil][self.personaje_col + 2] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil][self.personaje_col + 1] = self.personaje_meta 
            self.mapa[self.personaje_fil][self.personaje_col + 2] = self.caja_meta
            self.personaje_col = self.personaje_col + 1 
    #personaje_meta,caja,espacio      
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil][self.personaje_col + 1] == self.personaje
            and self.mapa[self.personaje_fil][self.personaje_col + 2] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil][self.personaje_col + 1] = self.personaje
            self.mapa[self.personaje_fil][self.personaje_col + 2] = self.caja
            self.personaje_col = self.personaje_col + 1                     
    #personaje_meta,espacio     
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil][self.personaje_col + 1] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil][self.personaje_col + 1] = self.personaje
            self.personaje_col = self.personaje_col + 1  
    #personaje_meta,meta     
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil][self.personaje_col + 1] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil][self.personaje_col + 1] = self.personaje_meta
            self.personaje_col = self.personaje_col + 1
    #personaje_meta,caja,espacio    
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil][self.personaje_col + 1] == self.caja
            and self.mapa[self.personaje_fil][self.personaje_col + 2] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil][self.personaje_col + 1] = self.personaje
            self.mapa[self.personaje_fil][self.personaje_col + 2] = self.caja
            self.personaje_col = self.personaje_col + 1 
    #personaje_meta,caja,meta   
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil][self.personaje_col + 1] == self.caja
            and self.mapa[self.personaje_fil][self.personaje_col + 2] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil][self.personaje_col + 1] = self.personaje
            self.mapa[self.personaje_fil][self.personaje_col + 2] = self.caja_meta
            self.personaje_col = self.personaje_col + 1    
    #personaje_meta,caja_meta,espacio   
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil][self.personaje_col + 1] == self.caja_meta
            and self.mapa[self.personaje_fil][self.personaje_col + 2] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil][self.personaje_col + 1] = self.personaje_meta
            self.mapa[self.personaje_fil][self.personaje_col + 2] = self.caja
            self.personaje_col = self.personaje_col + 1
    #personaje_meta,caja_meta,meta   
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil][self.personaje_col + 1] == self.caja_meta
            and self.mapa[self.personaje_fil][self.personaje_col + 2] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil][self.personaje_col + 1] = self.personaje_meta
            self.mapa[self.personaje_fil][self.personaje_col + 2] = self.caja_meta
            self.personaje_col = self.personaje_col + 1                     

  def moverIzquierda(self):
    print("te moviste a la izquierda") 

    #personaje,espacio(izquierda)
    if (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil][self.personaje_col - 1] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil][self.personaje_col - 1] = self.personaje  
            self.personaje_col = self.personaje_col - 1
    #personaje,meta(izquierda)
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil][self.personaje_col - 1] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil][self.personaje_col - 1] = self.personaje_meta  
            self.personaje_col = self.personaje_col - 1
     #personaje,caja,espacio(izquierda)     
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil][self.personaje_col - 1] == self.caja
            and self.mapa[self.personaje_fil][self.personaje_col - 2] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil][self.personaje_col - 1] = self.personaje 
            self.mapa[self.personaje_fil][self.personaje_col - 2] = self.caja
            self.personaje_col = self.personaje_col - 1
     #personaje,caja,meta(izquierda)     
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil][self.personaje_col - 1] == self.caja
            and self.mapa[self.personaje_fil][self.personaje_col - 2] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil][self.personaje_col - 1] = self.personaje 
            self.mapa[self.personaje_fil][self.personaje_col - 2] = self.caja_meta
            self.personaje_col = self.personaje_col - 1    
     #personaje,caja_meta,espacio(izquierda)     
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil][self.personaje_col - 1] == self.caja_meta
            and self.mapa[self.personaje_fil][self.personaje_col - 2] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil][self.personaje_col - 1] = self.personaje_meta 
            self.mapa[self.personaje_fil][self.personaje_col - 2] = self.caja
            self.personaje_col = self.personaje_col - 1 
     #personaje,caja_meta,meta(izquierda)    
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil][self.personaje_col - 1] == self.caja_meta
            and self.mapa[self.personaje_fil][self.personaje_col - 2] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil][self.personaje_col - 1] = self.personaje_meta 
            self.mapa[self.personaje_fil][self.personaje_col - 2] = self.caja_meta
            self.personaje_col = self.personaje_col - 1 
    #personaje_meta,caja,espacio(izquierda)      
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil][self.personaje_col - 1] == self.personaje
            and self.mapa[self.personaje_fil][self.personaje_col - 2] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil][self.personaje_col - 1] = self.personaje
            self.mapa[self.personaje_fil][self.personaje_col - 2] = self.caja
            self.personaje_col = self.personaje_col - 1                     
    #personaje_meta,espacio(izquierda)     
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil][self.personaje_col - 1] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil][self.personaje_col - 1] = self.personaje
            self.personaje_col = self.personaje_col - 1  
    #personaje_meta,meta(izquierda)     
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil][self.personaje_col - 1] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil][self.personaje_col - 1] = self.personaje_meta
            self.personaje_col = self.personaje_col - 1
    #personaje_meta,caja,espacio(izquierda)    
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil][self.personaje_col - 1] == self.caja
            and self.mapa[self.personaje_fil][self.personaje_col - 2] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil][self.personaje_col - 1] = self.personaje
            self.mapa[self.personaje_fil][self.personaje_col - 2] = self.caja
            self.personaje_col = self.personaje_col - 1 
    #personaje_meta,caja,meta(izquierda)   
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil][self.personaje_col - 1] == self.caja
            and self.mapa[self.personaje_fil][self.personaje_col - 2] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil][self.personaje_col - 1] = self.personaje
            self.mapa[self.personaje_fil][self.personaje_col - 2] = self.caja_meta
            self.personaje_col = self.personaje_col - 1    
    #personaje_meta,caja_meta,espacio(izquierda)   
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil][self.personaje_col - 1] == self.caja_meta
            and self.mapa[self.personaje_fil][self.personaje_col - 2] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil][self.personaje_col - 1] = self.personaje_meta
            self.mapa[self.personaje_fil][self.personaje_col - 2] = self.caja
            self.personaje_col = self.personaje_col - 1
    #personaje_meta,caja_meta,meta(izquierda)   
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil][self.personaje_col - 1] == self.caja_meta
            and self.mapa[self.personaje_fil][self.personaje_col - 2] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil][self.personaje_col - 1] = self.personaje_meta
            self.mapa[self.personaje_fil][self.personaje_col - 2] = self.caja_meta
            self.personaje_col = self.personaje_col - 1  

  def moverArriba(self):
    print("te moviste hacia arriba") 
    #personaje,espacio(arriba)
    if (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil - 1][self.personaje_col ] = self.personaje  
            self.personaje_fil = self.personaje_fil - 1
    #personaje,meta(arriba)
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil - 1][self.personaje_col] = self.personaje_meta  
            self.personaje_fil = self.personaje_fil - 1
     #personaje,caja,espacio(arriba)     
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.caja
            and self.mapa[self.personaje_fil - 2][self.personaje_col] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil - 1][self.personaje_col] = self.personaje 
            self.mapa[self.personaje_fil - 2][self.personaje_col] = self.caja
            self.personaje_fil = self.personaje_fil - 1
     #personaje,caja,meta(arriba)     
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.caja
            and self.mapa[self.personaje_fil - 2][self.personaje_col] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil - 1][self.personaje_col] = self.personaje 
            self.mapa[self.personaje_fil - 2][self.personaje_col] = self.caja_meta
            self.personaje_fil = self.personaje_fil - 1    
     #personaje,caja_meta,espacio(arriba)     
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.caja_meta
            and self.mapa[self.personaje_fil - 2][self.personaje_col] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil - 1][self.personaje_col] = self.personaje_meta 
            self.mapa[self.personaje_fil - 2][self.personaje_col] = self.caja
            self.personaje_fil = self.personaje_fil - 1 
     #personaje,caja_meta,meta(arriba)   
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.caja_meta
            and self.mapa[self.personaje_fil - 2][self.personaje_col] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil - 1][self.personaje_col] = self.personaje_meta 
            self.mapa[self.personaje_fil - 2][self.personaje_col] = self.caja_meta
            self.personaje_fil = self.personaje_fil - 1 
    #personaje_meta,caja,espacio(arriba)      
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil - 2][self.personaje_col] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil - 1][self.personaje_col] = self.personaje
            self.mapa[self.personaje_fil - 2][self.personaje_col] = self.caja
            self.personaje_fil = self.personaje_fil - 1                     
    #personaje_meta,espacio(arriba)    
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil - 1][self.personaje_col] = self.personaje
            self.personaje_fil = self.personaje_fil - 1  
    #personaje_meta,meta(arriba)     
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil - 1][self.personaje_col] = self.personaje_meta
            self.personaje_fil = self.personaje_fil - 1
    #personaje_meta,caja,espacio(arriba)    
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.caja
            and self.mapa[self.personaje_fil - 2][self.personaje_col] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil - 1][self.personaje_col] = self.personaje
            self.mapa[self.personaje_fil - 2][self.personaje_col] = self.caja
            self.personaje_fil = self.personaje_fil - 1 
    #personaje_meta,caja,meta(arriba)  
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.caja
            and self.mapa[self.personaje_fil - 2][self.personaje_col] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil - 1][self.personaje_col] = self.personaje
            self.mapa[self.personaje_fil - 2][self.personaje_col] = self.caja_meta
            self.personaje_fil = self.personaje_fil - 1    
    #personaje_meta,caja_meta,espacio(arriba)   
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.caja_meta
            and self.mapa[self.personaje_fil - 2][self.personaje_col] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil - 1][self.personaje_col] = self.personaje_meta
            self.mapa[self.personaje_fil - 2][self.personaje_col] = self.caja
            self.personaje_fil = self.personaje_fil - 1
    #personaje_meta,caja_meta,meta(arriba)   
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.caja_meta
            and self.mapa[self.personaje_fil - 2][self.personaje_col] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil - 1][self.personaje_col] = self.personaje_meta
            self.mapa[self.personaje_fil - 2][self.personaje_col] = self.caja_meta
            self.personaje_fil = self.personaje_fil - 1   

  def moverAbajo(self):
    print("te moviste hacia abajo") 
    #personaje,espacio(abajo)
    if (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil + 1][self.personaje_col] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil + 1][self.personaje_col ] = self.personaje  
            self.personaje_fil = self.personaje_fil + 1
    #personaje,meta(abajo)
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil + 1][self.personaje_col] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil + 1][self.personaje_col] = self.personaje_meta  
            self.personaje_fil = self.personaje_fil + 1
     #personaje,caja,espacio(abajo)     
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil + 1][self.personaje_col] == self.caja
            and self.mapa[self.personaje_fil + 2][self.personaje_col] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil + 1][self.personaje_col] = self.personaje 
            self.mapa[self.personaje_fil + 2][self.personaje_col] = self.caja
            self.personaje_fil = self.personaje_fil + 1
     #personaje,caja,meta(abajo)     
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil + 1][self.personaje_col] == self.caja
            and self.mapa[self.personaje_fil + 2][self.personaje_col] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil + 1][self.personaje_col] = self.personaje 
            self.mapa[self.personaje_fil + 2][self.personaje_col] = self.caja_meta
            self.personaje_fil = self.personaje_fil + 1    
     #personaje,caja_meta,espacio(abajo)     
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil + 1][self.personaje_col] == self.caja_meta
            and self.mapa[self.personaje_fil + 2][self.personaje_col] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil + 1][self.personaje_col] = self.personaje_meta 
            self.mapa[self.personaje_fil + 2][self.personaje_col] = self.caja
            self.personaje_fil = self.personaje_fil + 1 
     #personaje,caja_meta,meta(abajo)   
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil + 1][self.personaje_col] == self.caja_meta
            and self.mapa[self.personaje_fil + 2][self.personaje_col] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.espacio  
            self.mapa[self.personaje_fil + 1][self.personaje_col] = self.personaje_meta 
            self.mapa[self.personaje_fil + 2][self.personaje_col] = self.caja_meta
            self.personaje_fil = self.personaje_fil + 1 
    #personaje_meta,caja,espacio(abajo)      
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil + 1][self.personaje_col] == self.personaje
            and self.mapa[self.personaje_fil + 2][self.personaje_col] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil + 1][self.personaje_col] = self.personaje
            self.mapa[self.personaje_fil + 2][self.personaje_col] = self.caja
            self.personaje_fil = self.personaje_fil + 1                     
    #personaje_meta,espacio(arriba)    
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil - 1][self.personaje_col] = self.personaje
            self.personaje_fil = self.personaje_fil - 1  
    #personaje_meta,meta(arriba)     
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil - 1][self.personaje_col] = self.personaje_meta
            self.personaje_fil = self.personaje_fil - 1
    #personaje_meta,caja,espacio(arriba)    
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.caja
            and self.mapa[self.personaje_fil - 2][self.personaje_col] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil - 1][self.personaje_col] = self.personaje
            self.mapa[self.personaje_fil - 2][self.personaje_col] = self.caja
            self.personaje_fil = self.personaje_fil - 1 
    #personaje_meta,caja,meta(arriba)  
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.caja
            and self.mapa[self.personaje_fil - 2][self.personaje_col] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil - 1][self.personaje_col] = self.personaje
            self.mapa[self.personaje_fil - 2][self.personaje_col] = self.caja_meta
            self.personaje_fil = self.personaje_fil - 1    
    #personaje_meta,caja_meta,espacio(arriba)   
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.caja_meta
            and self.mapa[self.personaje_fil - 2][self.personaje_col] == self.espacio
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil - 1][self.personaje_col] = self.personaje_meta
            self.mapa[self.personaje_fil - 2][self.personaje_col] = self.caja
            self.personaje_fil = self.personaje_fil - 1
    #personaje_meta,caja_meta,meta(arriba)   
    elif (
            self.mapa[self.personaje_fil][self.personaje_col] == self.personaje_meta
            and self.mapa[self.personaje_fil - 1][self.personaje_col] == self.caja_meta
            and self.mapa[self.personaje_fil - 2][self.personaje_col] == self.meta
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = self.meta  
            self.mapa[self.personaje_fil - 1][self.personaje_col] = self.personaje_meta
            self.mapa[self.personaje_fil - 2][self.personaje_col] = self.caja_meta
            self.personaje_fil = self.personaje_fil - 1  
          

  

  def checharNivelCompleto(self):
        # TODO: Check if the level is complete
        # If return True, the level is complete
        # If return False, the level is not complete
        completo = False
        return completo
        
  def jugar(self):
        self.leerMapa()  # Call the map
        self.posicionPersonaje()  # Update the character position for new map
        instructions = "d-Derecha, a-Izquierda, w-Arriba, s-Abajo"  # Instructions
        print(instructions)  # Print the instructions
        while True:  # Infinite loop
            complete = self.checharNivelCompleto()  # Check if the level is complete
            if complete == True:  # If the level is complete
                print("Level Complete")  # Print the level complete
                input("Press Enter to continue...")  # Wait for the user to press enter
                self.leerMapa()  # Call the map
                self.posicionPersonaje()  # Update the character position for new map
            self.imprimirMapa()  # Call the printMap method 
            print(
                "Character position: [{},{}]".format(
                    self.personaje_fil, self.personaje_col
                )
            )  # Print the character position
            move = input("Select move: ")  # Ask for the move
            if move == "a":  # If the move is left
                self.moverIzquierda()  # Call moveLeft rules
            elif move == "d":  # If the move is right
                self.moverDerecha()  # Call moveRight rules
            elif move == "w":  # If the move is up
                self.moverArriba()  # Call moveUp rules
            elif move == "s":  # If the move is down
                self.moverAbajo()  # Call moveDown rules
            elif move == "q":  # If the move is quit
                break  # Game quit


game = Sokoban()  # Create a object from Sokoban class
game.jugar()