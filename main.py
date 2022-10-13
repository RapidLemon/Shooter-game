from modules import Game,Bullets
from modules.varibles import *
import pickle
import pygame
import neat
import os


clock = pygame.time.Clock()
x2,y2 = SCREEN_X-50,0

class ShooterGame:
    def run():
            """
            DONE
            """

            global x,y,x2,y2,boost,boost2,clock,bullet2s,bullets

            Running = True
            while Running:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        Running = False
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_ESCAPE:
                            Running = False
                            pygame.quit()
                            quit()

                        if event.key == pygame.K_SPACE:
                            boost = Game.space(1)

                        if event.key == pygame.K_UP:
                            boost2 = Game.space(0)

                        if event.key == pygame.K_DOWN:
                            Game.q_press(1)

                        if event.key == pygame.K_q:
                            Game.q_press(0)


                Keys = pygame.key.get_pressed()        

                if Keys[pygame.K_a]:
                    x = Game.a_press(1)

                if Keys[pygame.K_d]:
                    x = Game.d_press(1)

                if Keys[pygame.K_LEFT]:
                    x2 = Game.a_press(0)

                if Keys[pygame.K_RIGHT]:
                    x2 = Game.d_press(0)


                #-----------SCREEN STUFF-----------#

                Game.DrawScreen()
                Game.Draw_FPS(clock)

                #-----------PLAYER STUFF-----------#

                x,y = Game.Player_update(x,y,boost)
                x2,y2 = Game.Player2_update(x2,y2,boost2)
                x,y,boost = Game.Exit_script2(x,y)
                x2,y2,boost2 = Game.Exit_script2(x2,y2)

                #-----------BULLET STUFF-----------#
                bullet2s = Bullets.Bullet2s(bullet2s)
                bullets = Bullets.Bullets(bullets)
                Bullets.Bullet_Remove()

                playercheack = Game.CheakPlayerWin()
                if playercheack[1]:
                    if playercheack[0] == "Player2_won":
                        pygame.display.update()
                        print("Player2_won")
                        pygame.quit()
                    elif playercheack[0] == "Player_won":
                        pygame.display.update()
                        print("Player_won")
                        pygame.quit()


                clock.tick(60)
                pygame.display.update()

ShooterGame.run()
