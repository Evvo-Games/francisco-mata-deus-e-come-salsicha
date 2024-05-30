import pygame
from colors import *


width = 1024
height = 768

def main():
    
    # Inicializando o clock:
    clock = pygame.time.Clock()

    # Criando a janela:
    game_display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("FRANCISCO: Mata Deus e Come Salsicha")

    chico = pygame.image.load("media/sprites/chico/chicoFrente.png")
    chico_costas = pygame.image.load("media/sprites/chico/chicoCostas.png")
    chico_direita = pygame.image.load("media/sprites/chico/chicoLado.png")
    # chico_esquerda = pygame.transform.flip(chico_direita, True, False)

    #COMEÇANDO O JOGO
    running = True
    while running:
        #Usa o fps determinado anteriormente, 
        clock.tick(60)
        
        #Tratando eventos     
        for event in pygame.event.get():
           
            #Tornando possivel fechar o jogo
            if event.type == pygame.QUIT:
                running = False
        
        #Volta ao inicio do loop do jogo
        pygame.display.flip()

        game_display.fill(grey_color)
        game_display.blit(chico, (0, 0))
        
        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()