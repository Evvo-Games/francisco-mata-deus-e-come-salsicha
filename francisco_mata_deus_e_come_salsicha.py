import pygame


def main():

    # Inicializando o clock:
    clock = pygame.time.Clock()

    # Criando a janela:
    display = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("francisco mata deus e come salsicha")

    
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

if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()