"""
Steve Wills
11/8/24
Slide and Catch part 1
"""

import random, pygame, simpleGE

class Ball(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("golfball.png")
        self.setSize(25, 25)
        self.minSpeed = 5
        self.maxSpeed = 15
        self.reset()
        
    def reset(self):
        self.y = 15
        self.x = random.randint(15, 625)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
class TinCup(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("tincup.png")
        self.setSize(75, 75)
        self.position = (320, 400)
        self.moveSpeed = 10
    
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
        if self.isKeyPressed(pygame.K_UP):
            self.y -= self.moveSpeed
        if self.isKeyPressed(pygame.K_DOWN):
            self.y += self.moveSpeed
            
class Game(simpleGE.Scene):
        def __init__(self):
            super().__init__()
            self.setImage("BGC.png")
            self.sndBall = simpleGE.Sound("coin.wav")
            self.tinCup = TinCup(self)
            self.ball = Ball(self)
            self.sprites = [self.tinCup, self.ball]
        
        def process(self):
            if self.tinCup.collidesWith(self.ball):
                self.ball.reset()
                self.sndBall.play()
                
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
            