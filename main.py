import sys
import random

try:
    import pygame
except ImportError:
    print('pygame is most likely not installed:\n to fix, run command: py -m pip install pygame')


dis = (800,600)
root = pygame.display.set_mode(dis)

clock = pygame.time.Clock()
FPS = 60

cellWH = 20
rows = dis[1]//cellWH
cols = dis[0]//cellWH

ticksPerUpdate = 5

RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4


class snake():

    def __init__(self):

        self.applePos = [random.randint(0,cols-1),random.randint(0,rows-1)]

        self.segments = [[0,0],[1,0]]
        self.head = [2,0]

        self.direction = RIGHT

        self.add = 0

        self.dead = False

    def update(self):

        if self.head == self.applePos or self.applePos in self.segments:
            self.add += 10
            self.applePos = [random.randint(0,cols-1),random.randint(0,rows-1)]

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and self.direction != LEFT:
            self.direction = RIGHT
        if keys[pygame.K_a] and self.direction != RIGHT:
            self.direction = LEFT
        if keys[pygame.K_s] and self.direction != DOWN:
            self.direction = DOWN
        if keys[pygame.K_w] and self.direction != UP:
            self.direction = UP


        self.segments.append(self.head.copy())

        if self.add == 0:
            del self.segments[0]
        else:
            self.add -= 1

        if (self.direction == RIGHT):
            self.head[0] += 1
        elif (self.direction == LEFT):
            self.head[0] -= 1
        elif (self.direction == UP):
            self.head[1] -= 1
        elif (self.direction == DOWN):
            self.head[1] += 1

        if self.head in self.segments or self.head[0] > cols-1 or self.head[0] < 0 or self.head[1] > rows-1 or self.head[1] < 0:
            self.dead = True

    def draw(self,root):
        pygame.draw.rect(root,(255,0,0),(self.head[0]*cellWH,self.head[1]*cellWH,cellWH,cellWH))

        for segment in self.segments:
            pygame.draw.rect(root,(255,0,0),(segment[0]*cellWH,segment[1]*cellWH,cellWH,cellWH))

        pygame.draw.rect(root,(0,255,0),(self.applePos[0]*cellWH,self.applePos[1]*cellWH,cellWH,cellWH))
        
        if self.dead:
            self.reset()
            self.dead = False

    def reset(self):
        self.applePos = [random.randint(0,cols),random.randint(0,rows)]

        self.segments = [[0,0],[1,0]]
        self.head = [2,0]

        self.direction = RIGHT

        self.add = 0



def main(args):

    s = snake()

    frame = 0

    while True:
        frame += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        root.fill((0,0,0))

        if (frame > ticksPerUpdate):
            frame -= ticksPerUpdate
            s.update()

        s.draw(root)

        pygame.display.update()
        clock.tick(FPS)



if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as e:
        pygame.quit()
        raise e
