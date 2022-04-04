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
        [3,1,1,1,1,1,0,1,1,1,1,3],
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
          if self.mapa[fil][col] == 0: 
            self.personaje_fil = fil 
            self.personaje_col = col 

  def moverDerecha(self):
    print("te moviste a las derecha")#en lujar del 0, self.personaje, 1 = self.espacio
    if (
            self.mapa[self.personaje_fil][self.personaje_col] == 0
            and self.mapa[self.personaje_fil][self.personaje_col + 1] == 1
        ):  # If the character is on the floor and the next position is a floor
            self.mapa[self.personaje_fil][self.personaje_col] = 1  # put floor character last position
            self.mapa[self.personaje_fil][self.personaje_col + 1] = 0  # move the character to next position
            self.personaje_col = self.personaje_col + 1



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