import pygame

def screen_with(Screensize = "half"):
    global SCREEN_X,SCREEN_Y
    if Screensize == "full":
        infoObject = pygame.display.Info()
        SCREEN_X,SCREEN_Y = infoObject.current_w, infoObject.current_h
    elif Screensize == "half":
        SCREEN_X,SCREEN_Y = 1000,800


#SCREEN_X,SCREEN_Y = infoObject.current_w, infoObject.current_h
#SCREEN_X,SCREEN_Y = 1000,800

pygame.init()
pygame.display.init()
Clock = pygame.time.Clock()
screen_with()
screen = pygame.display.set_mode((SCREEN_X,SCREEN_Y))
BACKGOUND_COLOUR = (200,200,200)
FLOOR_COLOUR = (40,40,40)
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAVITY = 0.38
FLOOR_Y = SCREEN_Y*0.8
bullet2sremove = []
bulletsremove = []
bullets = []
bullet2s = []
vel = GRAVITY
vel2 = GRAVITY
x,y = 50,0
x2,y2 = SCREEN_X-50,0
count = 0
Player_won = False
Player2_won = False
running = True



def Exit_script(x,y,x2,y2,boost = 0,boost2 = 0):
    global running,vel,vel2

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                quit()

            if event.key == pygame.K_SPACE:
                vel = 0
                boost = Player.Move.up()

            if event.key == pygame.K_UP:
                boost2,vel2 = Player2.K_UP(vel2,boost2)

            if event.key == pygame.K_DOWN:
                bullet2s.append([x2, y2,Player.get_pos("x") <= Player2.get_pos("x"),vel2/3])

            if event.key == pygame.K_q:
                bullets.append([x,y,Player.get_pos("x") <= Player2.get_pos("x"),vel/3])
                

    Keys = pygame.key.get_pressed()        

    if Keys[pygame.K_a]:
        x = Player.Move.left(x)

    if Keys[pygame.K_d]:
        x = Player.Move.right(x)


    if Keys[pygame.K_LEFT]:
        x2 = Player2.K_LEFT(x2)

    if Keys[pygame.K_RIGHT]:
        x2 = Player2.K_RIGHT(x2)

    return x,y,boost,x2,y2,boost2


def DrawScreen():
    screen.fill(BACKGOUND_COLOUR)
    pygame.draw.rect(screen,FLOOR_COLOUR,(0,FLOOR_Y,SCREEN_X,SCREEN_Y))
    pygame.draw.line(screen,BLACK,(0,FLOOR_Y),(SCREEN_X,FLOOR_Y),(5))

def Player_update(x_,y_,boost):
    x,y = Player.MoveX(x_),Player.Update_gravity(y_,boost)
    Player.draw(x,y)

    return x,y

def Player2_win():
    global Player2_won
    Player2_won = True

def Player_win():
    global Player_won
    Player_won = True

def Wait_frames(frames):
    global count

    if count == frames:
        return True
    else:
        count += 1
        return False



class Player:
    def draw(x,y):
        pygame.draw.circle(screen,(BLACK),(x,y),15)
        pygame.draw.circle(screen,(WHITE),(x,y),12)
        pygame.draw.circle(screen,(0,0,255),(x,y),4)

    def Update_gravity(y, boost):
        global vel

        vel -= boost
                
        y += vel
        vel = round(vel + GRAVITY,2)

        y,vel = Player.CheackPos(y,vel)
        return y

    def MoveX(x, x_move = 0):
        x += x_move
        
        if x <= 0 + 15:
            x = 0 + 15
        
        if x >= SCREEN_X - 15:
            x = SCREEN_X - 15

        return x

    def Jump():
        boost = 8
        return boost


    def CheackPos(y2,vel2):

        if y2 >= FLOOR_Y-15:
            y2 = FLOOR_Y-15
            vel2 = 0
        
        if y2 <= 0:
            vel2 = 20
            y2 = 0
        
        return y2, vel2

    def get_pos(xy = "h"):
        if xy == "x":
            return x
        elif xy == "y":
            return y
        else:
            return x,y

    class Move:
        
        def left(x,speed = 10):
            move = x - speed
            return move

        def right(x,speed = 10):
            move = x + speed
            return move

        def up():
            if Player.get_pos("y") >= 0:
                return Player.Jump()
            else:
                return 0


def Exit_script2(x,y,boost2 = 0):
    global vel2
            
    return x,y,boost2


def Player_update2(x_,y_,boost2):
    x,y = Player2.MoveX(x_),Player2.Update_gravity(y_,boost2)
    Player2.draw(x,y)

    return x,y


class Player2:

    def K_UP(vel2,boost2):
        vel2 = 0
        boost2 = Player2.Move2.up()
        return boost2,vel2

    def K_RIGHT(x2):
        x2 = Player2.Move2.right(x2)
        return x2

    def K_LEFT(x2):
        x2 = Player2.Move2.left(x2)
        return x2


    def draw(x,y):
        pygame.draw.circle(screen,(BLACK),(x,y),15)
        pygame.draw.circle(screen,(WHITE),(x,y),12)
        pygame.draw.circle(screen,(255,0,0),(x,y),4)

    def Update_gravity(y2, boost2):
        global vel2

        vel2 -= boost2
                
        y2 += vel2
        vel2 = round(vel2 + GRAVITY,2)

        y2,vel2 = Player2.CheackPos(y2,vel2)
        print(y2,vel2)
        return y2

    def MoveX(x, x_move = 0):
        x += x_move
        
        if x <= 0 + 15:
            x = 0 + 15
        
        if x >= SCREEN_X - 15:
            x = SCREEN_X - 15

        return x

    def Jump():
        boost2 = 8
        return boost2


    def CheackPos(y2,vel2):

        if y2 >= FLOOR_Y-15:
            y2 = FLOOR_Y-15
            vel2 = 0

        if y2 <= 0:
            vel2 = 20
            y2 = 0

        return y2, vel2

    def get_pos(xy = "h"):
        if xy == "x":
            return x2
        elif xy == "y":
            return y2
        else:
            return x2,y2

    class Move2:
        
        def left(x,speed = 10):
            move = x - speed
            return move

        def right(x,speed = 10):
            move = x + speed
            return move

        def up():
            if Player2.get_pos("y") >= 0:
                return Player2.Jump()
            else:
                return 0

class Bullets:
    def Bullet2s():
        for bullet in bullet2s:
            Bullets.Bullet2.draw(bullet[0],bullet[1])
            bullet[0], bullet[1] = Bullets.Bullet2.shoot(bullet[0],bullet[1],bullet[2],bullet[3])
            if Bullets.Bullet2.cheackpos(bullet[0],bullet[1]):
                bullet2sremove.append(bullet)

    def Bullets():
        for bullet in bullets:
                Bullets.Bullet.draw(bullet[0],bullet[1])
                bullet[0], bullet[1] = Bullets.Bullet.shoot(bullet[0],bullet[1],bullet[2],bullet[3])
                if Bullets.Bullet.cheackpos(bullet[0],bullet[1]):
                    bulletsremove.append(bullet)

    def Bullet_Remove():
        for bullet in bullet2sremove:
            bullet2s.remove(bullet2sremove[0])
            bullet2sremove.remove(bullet2sremove[0])

        for bullet in bulletsremove:
            bullets.remove(bulletsremove[0])
            bulletsremove.remove(bulletsremove[0])


    class Bullet:

        def draw(bulletx,bullety):
            pygame.draw.rect(screen,(0,0,255),(bulletx,bullety,15,5))
            pygame.draw.ellipse(screen,(0,0,255),(bulletx+5, bullety, 15,5))

        def shoot(bulletx,bullety,dir,vel):
            if not dir:
                bulletx -= 20
            else:
                bulletx += 20

            bullety -= vel
            return bulletx,bullety

        def cheackpos(bulletx,bullety):
            if bulletx+12 > Player2.get_pos("x") and bulletx-12 < Player2.get_pos("x") and bullety+7.5 > Player2.get_pos("y") and bullety-7.5 < Player2.get_pos("y"):
                Player_win()
                return True
            elif bulletx >= SCREEN_X:
                return True
            
            elif bulletx <= 0:
                return True
            
            else:
                return False

    class Bullet2:

        def draw(bullet2x,bullet2y):
            pygame.draw.rect(screen,(255,0,0),(bullet2x,bullet2y,15,5))
            pygame.draw.ellipse(screen,(255,0,0),(bullet2x-5, bullet2y, 15,5))

        def shoot(bullet2x,bullet2y,dir,vel):
            if dir:
                bullet2x -= 20
            else:
                bullet2x += 20

            bullet2y -= vel
            return bullet2x,bullet2y

        def cheackpos(bullet2x,bullet2y):
            if bullet2x+12 > Player.get_pos("x") and bullet2x-12 < Player.get_pos("x") and bullet2y+7.5 > Player.get_pos("y") and bullet2y-7.5 < Player.get_pos("y"):
                Player2_win()
                return True

            elif bullet2x <= 0:
                return True
            
            elif bullet2x >= SCREEN_X:
                return True
            
            else:
                return False


'''while running:

    DrawScreen()

    boost,boost2 = 0,0

    #"""
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                quit()

            if event.key == pygame.K_SPACE:
                vel = 0
                boost = Player.Move.up()

            if event.key == pygame.K_UP:
                boost2,vel2 = Player2.K_UP(vel2,boost2)

            if event.key == pygame.K_DOWN:
                bullet2s.append([x2, y2,Player.get_pos("x") <= Player2.get_pos("x"),vel2/3])

            if event.key == pygame.K_q:
                bullets.append([x,y,Player.get_pos("x") <= Player2.get_pos("x"),vel/3])
                

    Keys = pygame.key.get_pressed()        

    if Keys[pygame.K_a]:
        x = Player.Move.left(x)

    if Keys[pygame.K_d]:
        x = Player.Move.right(x)


    if Keys[pygame.K_LEFT]:
        x2 = Player2.K_LEFT(x2)

    if Keys[pygame.K_RIGHT]:
        x2 = Player2.K_RIGHT(x2)
    #"""

     
    #x_,y_,boost,x_2,y_2,boost2 = Exit_script(x,y,x2,y2)    
    x,y = Player_update(x,y,boost)
    x2,y2 = Player_update2(x2,y2,boost2)

    Bullets.Bullet2s()
    Bullets.Bullets()
    Bullets.Bullet_Remove()

    if Player2_won:
        Player.draw(x,y)
        pygame.display.update()
        print("Player2_won")
        break
    elif Player_won:
        Player2.draw(x2,y2)
        pygame.display.update()
        print("Player_won")
        break

    Clock.tick(60)
    pygame.display.update()

pygame.quit()'''