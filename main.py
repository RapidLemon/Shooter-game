import mods.game_loop as gameloop
from math import sqrt
import neat 
import os

x,y,z = 50,0,0
x2,y2 = gameloop.SCREEN_X-50,0

class Game:
    def train_ai(genome1, genome2, config):
        global x,y,x2,y2,z
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

        z += 1

        run = True
        while run:
            for event in gameloop.pygame.event.get():
                
                if event.type == gameloop.pygame.QUIT:
                    quit()

                if event.type == gameloop.pygame.KEYDOWN:
                    
                    if event.key == gameloop.pygame.K_ESCAPE:
                        gameloop.running = False
                        gameloop.pygame.quit()
                        quit()

            if len(gameloop.bullets) != 0:
                for i in gameloop.bullets:
                    temp = 10000
                    distlist = sqrt((gameloop.bullets[i][0] - gameloop.Player.get_pos("x"))**2 + (gameloop.bullets[i][1] - gameloop.Player.get_pos("y"))**2)
                for i in gameloop.bullets:
                    if distlist[i] < temp:
                        temp = distlist[1]
                dist = temp
            else:
                dist = 99999999

            if len(gameloop.bullet2s) != 0:
                for i in gameloop.bullet2s:
                    temp = 10000
                    distlist = sqrt((gameloop.bullet2s[i][0] - gameloop.Player.get_pos("x"))**2 + (gameloop.bullet2s[i][1] - gameloop.Player.get_pos("y"))**2)
                for i in gameloop.bullet2s:
                    if distlist[i] < temp:
                        temp = distlist[1]
                dist2 = temp
            else:
                dist2 = 99999999999

            output1 = net1.activate(((gameloop.Player.get_pos("y")), (gameloop.Player.get_pos("x")),(gameloop.Player2.get_pos("x")),(gameloop.Player2.get_pos("y")),gameloop.vel,gameloop.vel2,len(gameloop.bullets),len(gameloop.bullet2s),abs(dist)))
            output2 = net2.activate(((gameloop.Player.get_pos("y")), (gameloop.Player.get_pos("x")),(gameloop.Player2.get_pos("x")),(gameloop.Player2.get_pos("y")),gameloop.vel,gameloop.vel2,len(gameloop.bullets),len(gameloop.bullet2s),abs(dist2)))

            print(z)

            x,y = gameloop.Player_update(x,y,8)
            x2,y2 = gameloop.Player_update2(x2,y2,8)

            gameloop.Bullets.Bullet2s()
            gameloop.Bullets.Bullets()
            gameloop.Bullets.Bullet_Remove()

            if gameloop.Player2_won:
                gameloop.Player.draw(gameloop.x,gameloop.y)
                gameloop.pygame.display.update()
                print("Player2_won")
                break
            elif gameloop.Player_won:
                gameloop.Player2.draw(gameloop.x2,gameloop.y2)
                gameloop.pygame.display.update()
                print("Player_won")
                break

            gameloop.pygame.display.update()





    def rungame():
        gameloop.screen_with(Screensize = "full")

        while gameloop.running:

            gameloop.DrawScreen()

            gameloop.boost,gameloop.boost2 = 0,0

            for event in gameloop.pygame.event.get():
                
                if event.type == gameloop.pygame.QUIT:
                    gameloop.running = False
                    gameloop.pygame.quit()
                    quit()
                if event.type == gameloop.pygame.KEYDOWN:
                    
                    if event.key == gameloop.pygame.K_ESCAPE:
                        gameloop.running = False
                        gameloop.pygame.quit()
                        quit()

                    if event.key == gameloop.pygame.K_SPACE:
                        gameloop.vel = 0
                        gameloop.boost = gameloop.Player.Move.up()

                    if event.key == gameloop.pygame.K_UP:
                        gameloop.boost2,gameloop.vel2 = gameloop.Player2.K_UP(gameloop.vel2,gameloop.boost2)

                    if event.key == gameloop.pygame.K_DOWN:
                        gameloop.bullet2s.append([gameloop.x2, gameloop.y2,gameloop.Player.get_pos("x") <= gameloop.Player2.get_pos("x"),gameloop.vel2/3])

                    if event.key == gameloop.pygame.K_q:
                        gameloop.bullets.append([gameloop.x,gameloop.y,gameloop.Player.get_pos("x") <= gameloop.Player2.get_pos("x"),gameloop.vel/3])
                        

            Keys = gameloop.pygame.key.get_pressed()        

            if Keys[gameloop.pygame.K_a]:
                gameloop.x = gameloop.Player.Move.left(gameloop.x)

            if Keys[gameloop.pygame.K_d]:
                gameloop.x = gameloop.Player.Move.right(gameloop.x)


            if Keys[gameloop.pygame.K_LEFT]:
                gameloop.x2 = gameloop.Player2.K_LEFT(gameloop.x2)

            if Keys[gameloop.pygame.K_RIGHT]:
                gameloop.x2 = gameloop.Player2.K_RIGHT(gameloop.x2)

            
            gameloop.x,gameloop.y = gameloop.Player_update(gameloop.x,gameloop.y,gameloop.boost)
            gameloop.x2,gameloop.y2 = gameloop.Player_update2(gameloop.x2,gameloop.y2,gameloop.boost2)

            gameloop.Bullets.Bullet2s()
            gameloop.Bullets.Bullets()
            gameloop.Bullets.Bullet_Remove()

            if gameloop.Player2_won:
                gameloop.Player.draw(gameloop.x,gameloop.y)
                gameloop.pygame.display.update()
                print("Player2_won")
                break
            elif gameloop.Player_won:
                gameloop.Player2.draw(gameloop.x2,gameloop.y2)
                gameloop.pygame.display.update()
                print("Player_won")
                break

            gameloop.Clock.tick(60)
            gameloop.pygame.display.update()

        gameloop.pygame.quit()

def eval_genomes(genomes, config):
    infoObject = gameloop.pygame.display.Info()
    SCREEN_X,SCREEN_Y = infoObject.current_w, infoObject.current_h
    win = gameloop.pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    gameloop.pygame.display.set_caption("Pong")

    for i,(genome_id1, genome1) in enumerate(genomes):
        if i == len(genomes) - 1:
            break
        genome1.fitness = 0
        for genome_id2, genome2 in genomes[i+1:]:
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            #game = Game.rungame()
            Game.train_ai(genome1, genome2, config)

def run_neat(config):
    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-85')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    winner = p.run(eval_genomes, 50)


if __name__ == "_main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,neat.DefaultSpeciesSet, neat.DefaultStagnation,config_path)

#run_neat(config)
Game.rungame()