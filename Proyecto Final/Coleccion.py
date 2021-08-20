import os
#Cración de un menú
op='1'
while(op!='3'):
    os.system("cls")
    # Mensaje de bienvenida
    print("\n\n\t\t\tBienvenid@")
    print("\n\t1) Jugar Snake\n \t2) Jugar Breakout\n \t3) Salir\n")
    op=input("\n\tElige una opción: ")
    if op == '1':
        import pygame
        #Se usa para la comida
        import random

        #Clase que corresponde al cuerpo de la serpiente
        class cuerpo:
            def __init__(self, ventana):
                #Posición inicial de la serpiente
                self.x = 0
                self.y = 0
                #Direccion que dirá hacia donde se mueve el cuerpo
                self.dir = 0
                self.ventana = ventana

            #Función para dibujar el cuerpo de la serpiente
            def dibujar(self):
                pygame.draw.rect(self.ventana, (255, 255, 255), (self.x, self.y, 10, 10))

            #Función para que el cuerpo se mueva
            def moverse(self):
                if self.dir == 0:
                    self.x += 10
                elif self.dir == 1:
                    self.x -= 10
                elif self.dir == 2:
                    self.y += 10
                elif self.dir == 3:
                    self.y -= 10

        #Clase que corresponde a la comida de la serpiente
        class manzanas:
            def __init__(self, ventana):
                #La posición de la comida es aleatoria
                self.x = random.randrange(40) * 10
                self.y = random.randrange(40) * 10
                self.ventana = ventana

            #Función que corresponde al cuerpo de la serpiente
            def dibujar(self):
                #Color de la serpiente (255, 0, 0)
                pygame.draw.rect(self.ventana, (255, 0, 0), (self.x, self.y, 10, 10))

            def nueva_manzana(self):
                self.x = random.randrange(40) * 10
                self.y = random.randrange(40) * 10

        #Función para dibujar constantemente en la ventana
        def refrescar(ventana):
            #Llenado de color negro
            ventana.fill((0, 0, 0))
            #Dibujar la comida
            comida.dibujar()
            #Como la serpiente va a tener varias partes se usa el ciclo for
            for i in range(len(serpiente)):
                #Dibujar a la serpiente
                serpiente[i].dibujar()

        #Función que va a seguir a la cabeza
        def seguir_cabeza():
            #A todas las posiciones
            for i in range(len(serpiente) - 1):
                '''
                La última posición de la serpiente va a ser igual a la penúltima
                posición y asi sucesivamente hasta que la segunda posición sea igual 
                a la cabeza, tanto en x como en y
                '''
                serpiente[len(serpiente) - i - 1].x = serpiente[len(serpiente) - i - 2].x
                serpiente[len(serpiente) - i - 1].y = serpiente[len(serpiente) - i - 2].y

        #Función principal
        def main():
            #Variable global
            global serpiente, comida
            #Para ventana de Juego
            ventana = pygame.display.set_mode((400, 400))
            ventana.fill((0, 0, 0))
            comida = manzanas(ventana)
            #Serpiente va a ser una lista
            serpiente = [cuerpo(ventana)]

            #Variable
            run = True
            #Estructura de repetición while
            while run:
                #Estructura de repeteción for
                for event in pygame.event.get():
                    #Si se sale del programa entonces la variable run sera falsa
                    if event.type == pygame.QUIT:
                        run = False
                    #Cambiar la dirección con los teclados
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            #Cambiar la dirección de la cabeza
                            serpiente[0].dir = 0
                        if event.key == pygame.K_LEFT:
                            #Cambiar la dirección de la cabeza
                            serpiente[0].dir = 1
                        if event.key == pygame.K_DOWN:
                            #Cambiar la dirección de la cabeza
                            serpiente[0].dir = 2
                        if event.key == pygame.K_UP:
                            # Cambiar la dirección de la cabeza
                            serpiente[0].dir = 3

                #Cada vez que el código corra la serpiente se debe mover
                serpiente[0].moverse()
                #Llamar a la función refrescar
                refrescar(ventana)
                #Refrescar la ventana completamente
                pygame.display.update()
                #Establece la velocidad que tarda en girar
                pygame.time.delay(96)
                #Cada vez que coma la serpiente debe crecer
                if serpiente[0].x == comida.x and serpiente[0].y == comida.y:
                    comida.nueva_manzana()
                    #A la serpiente le vamos a añadir una nueva función
                    serpiente.append(cuerpo(ventana))
                #Para que el cuerpo siga a la cabeza de la serpiente
                seguir_cabeza()
                #Si la cabeza de la serpiente se sale de la pantalla se movera la cabeza a la posición 0
                if serpiente[0].x >= 400:
                    serpiente[0].x = 0
                #Si la cabeza esta en una posición menor a cero tiene que ir a la posición donde inicia la pantalla
                elif serpiente[0].x < 0:
                    serpiente[0].x = 390
                if serpiente[0].y >= 400:
                    serpiente[0].y = 0
                elif serpiente[0].y < 0:
                    serpiente[0].y = 390

        if __name__ == '__main__':
            main()
            # Salida del programa
            pygame.quit()

    elif op =='2':

        #Librería pygame
        import pygame

        class pelota:
            #Función que define la posición de la pelota
            def __init__(self, ventana, x, y):
                self.ventana = ventana
                self.x = x
                self.y = y
                self.vx = 0
                self.vy = 0

            #Función para dibujar a la pelota
            def dibujar(self):
                #Se define el color y tamaño de la pelota
                pygame.draw.rect(self.ventana, (255, 255, 255), (self.x, self.y, 10, 10))

            #Función para mover a la pelota
            def mover(self):
                #Los movimientos se realizan de acuerdo a la posición
                self.x += self.vx
                self.y += self.vy

        #Definir la plataforma en la que rebotará
        class Raqueta:
            def __init__(self, ventana):
                #Definir el tamaño de la plataforma
                self.tamano = 80
                #Definir la pocisión de la plataforma
                self.x = 600 / 2 - self.tamano / 2
                self.y = 380
                self.centro = self.x + self.tamano / 2
                self.ventana = ventana
                #Variables para que se mueva la plataforma
                self.izq = False
                self.der = False

            #Función para dibujar la plataforma en la ventana
            def dibujar(self):
                pygame.draw.rect(self.ventana, (255, 255, 255), (self.x, self.y, self.tamano, 10))

            #Función para definir el movimiento de la plataforma
            def mover(self):
                if self.izq: self.x -= 10
                if self.der: self.x += 10
                #Poner limites para que la plataforma no se salga de la pantalla
                self.x = 0 if self.x < 0 else 600 - self.tamano if self.x + self.tamano > 600 else self.x
                self.centro = self.x + self.tamano / 2

        #Creación de una clase para los bloques superiores
        class Bloques:
            def __init__(self, ventana):
                self.ventana = ventana
                #Creación de los bloques a destruir
                self.tablero = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

            #Función para dibujar el tablero en la pantalla
            def dibujar(self):
                for i in range(4):
                    for j in range(10):
                        if self.tablero[i][j] != 0:
                            #Darle un color al tablero
                            if self.tablero[i][j] == 4:
                                color = (255, 255, 255)
                            elif self.tablero[i][j] == 3:
                                color = (55, 255, 255)
                            elif self.tablero[i][j] == 2:
                                color = (55, 55, 255)
                            elif self.tablero[i][j] == 1:
                                color = (255, 55, 255)
                            pygame.draw.rect(self.ventana, color, (j * 60, i * 10 + 35, 59, 9))

        #Función para refrescar la ventana
        def refrescar(ventana):
            #Llenado de la ventana
            ventana.fill((0, 0, 0))
            #Dibujar la pelota en la ventana
            bola.dibujar()
            #Dibujar la plataforma en la ventana
            r1.dibujar()
            #Mostrar el tablero
            tablero.dibujar()
            #Dibujar el texto
            text = font.render(str(golpes), True, ((255, 255, 255)))
            text_rect = text.get_rect()
            #Centrar el texto
            text_rect.centerx = 300
            ventana.blit(text, text_rect)

        #Función que se encargará de evaluar los golpes con el tablero
        def colisiones():
            global golpes
            if bola.y < 3 * 10 + 35 + 9:
                for i in range(4):
                    for j in range(10):
                        if tablero.tablero[i][j] != 0:
                            if ((j * 60 < bola.x < j * 60 + 59) or (j * 60 < bola.x + 10 < j * 60 + 59)) and (
                                    (i * 10 + 35 < bola.y < i * 10 + 35 + 9) or (
                                    i * 10 + 35 < bola.y + 10 < i * 10 + 35 + 9)):
                                #Borrar un bloque cuando sea golpeado
                                tablero.tablero[i][j] = 0
                                #La pelota rebotará al golpear un bloque
                                bola.vy *= -1
                                #Los golpes solo se contarán cuando la pelota rompa el tablero
                                golpes += 1

        #Función principal
        def main():
            #Generar una varible global
            global bola, golpes, font, r1, tablero
            #Creación de ventana
            ventana = pygame.display.set_mode((600, 400))
            #Rellenado de la ventana
            ventana.fill((0, 0, 0))
            bola = pelota(ventana, 50, 100)
            #Asignarle velocidad a la pelota
            bola.vx = 5
            bola.vy = 2
            golpes = 0
            #Aparición de texto en la pantalla
            pygame.font.init()
            font = pygame.font.SysFont("Arial", 30)
            #Variable que va a permitir hacer el ciclo while
            jugar = True
            #Variable para la plataforma
            r1 = Raqueta(ventana)
            tablero = Bloques(ventana)
            #Varible reloj
            clock = pygame.time.Clock()
            #Ciclo while
            while jugar:
                #Eventos que se generán
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        jugar = False
                    #Movimiento de la plataforma de acuerdo a la tecla oprimida
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            r1.izq = True
                        if event.key == pygame.K_RIGHT:
                            r1.der = True
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            r1.izq = False
                        if event.key == pygame.K_RIGHT:
                            r1.der = False
                #Para mover a la pelota
                bola.mover()
                r1.mover()
                #Llamar a la función colisiones
                colisiones()
                #Definir que la pelota se golpee contra los muros
                if bola.x >= 590:
                    bola.vx *= -1
                    bola.x = 590
                if bola.x <= 0:
                    bola.vx *= -1
                    bola.x = 0
                #Hacer que la pelota rebote en la plataforma
                if bola.y + 10 > r1.y:
                    if (r1.x < bola.x < r1.x + r1.tamano) or (r1.x < bola.x + 10 < r1.x + r1.tamano):
                        #Variable que va adefinir el porcentaje de las velocidades dependiendo del lugar de impacto de la pelota
                        porcentaje = (bola.x - r1.centro) / (r1.tamano / 2)
                        bola.vx += porcentaje * 10
                        bola.vx = -10 if bola.vx < -10 else 10 if bola.vx > 10 else bola.vx
                        bola.vy *= -1
                        bola.y = r1.y - 10
                    elif bola.y > 400:
                        bola.y = 100
                if bola.y <= 0:
                    bola.vy *= -1
                    bola.y = 0
                #Llamar a la función refrescar
                refrescar(ventana)
                clock.tick(60)
                pygame.display.update()

        if __name__ == '__main__':
            main()
            pygame.quit()
    elif op =='3':
        #Mensaje en caso de elegir la opción salir
        print("\n\tElegiste salir, Gracias por usar mi programa")
        input("\n\tPresiona enter para salir...")
    else:
        #Mensaje en caso de elegir una opción que no venga en el menú
        print("\n\t***OPCIÓN NO VALIDA***")
        input("\n\tPresiona enter para continuar...")


1
